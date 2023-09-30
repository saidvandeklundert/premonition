from pydantic import BaseModel
from premonition import LLDP, LLDPInterface
from .lexer import Lexer
from .configwriter import ConfigWriter


from premonition import System, Vlans, Vlan


class DeviceModel(BaseModel):
    """
    Vendor agnostic representation of a network node.
    """

    system: System | None = None
    lldp: LLDP | None = None
    vlans: Vlans | None = None


class Device(BaseModel):
    """
    Model of a device
    """

    hostname: str
    configuration: str
    model: DeviceModel = DeviceModel()

    def show_model(self):
        return self.model_dump_json(indent=4, exclude="configuration")


class JuniperDevice(Device):
    """
    Variant specific for Juniper devices.
    """

    configuration_set_style: str | None = None

    def show_model(self):
        return self.model_dump(
            exclude="configuration,configuration_set_style", exclude_defaults=True
        )

    def show_model_json(self):
        return self.model_dump_json(
            indent=4, exclude="configuration,configuration_set_style"
        )

    def build_models(self) -> None:
        """
        Build the models from the device configuration.
        """
        lexer = Lexer(source=self.configuration)
        lexer.read_tokens()
        cw = ConfigWriter(tokens=lexer.tokens)
        self.configuration_set_style = cw.build_set_config()
        lldp_model = self.lldp_builder()
        self.model.lldp = lldp_model
        self.system_builder()
        self.vlans_builder()
        return None

    def lldp_builder(self) -> LLDP:
        """
        Builds a model that represents the LLDP configuration of the node.
        """
        lldp_config = "\n".join(
            [
                line
                for line in self.configuration_set_style.splitlines()
                if "set protocols lldp" in line
            ]
        )
        lldp_model = LLDP()

        for line in lldp_config.splitlines():
            line_parts = line.split()
            lldp_identifier = line_parts[3]
            match lldp_identifier:
                case "interface":
                    lldp_interface_builder(lldp_model=lldp_model, line_parts=line_parts)
                case _:
                    lldp_model.features.add(" ".join(line_parts[3::]))
        return lldp_model

    def system_builder(self):
        system_config = [
            line
            for line in self.configuration_set_style.splitlines()
            if line.startswith("set system")
        ]

        self.model.system = System()
        for line in system_config:
            parts = line.split()
            # syslog
            if "set system syslog host" in line and len(parts) >= 4:
                syslog_server_ip = parts[4]
                self.model.system.syslog.servers.append(syslog_server_ip)
            # name-server
            if "set system name-server" in line and len(parts) >= 4:
                name_server_ip = parts[3]
                self.model.system.name_servers.servers.append(name_server_ip)
            # ntp-server
            if "set system ntp server" in line and len(parts) >= 4:
                ntp_server = parts[4]
                self.model.system.ntp.servers.append(ntp_server)

    def vlans_builder(self):
        vlans_config = [
            line
            for line in self.configuration_set_style.splitlines()
            if line.startswith("set vlans")
        ]
        vlans_model = Vlans()
        l3_interfaces = {}
        for line in vlans_config:
            parts = line.split()
            if len(parts) == 5 and parts[3] == "vlan-id":
                vlan_id = int(parts[4])
                vlan_name = parts[2]
                vlans_model.vlans[vlan_id] = Vlan(vlan_id=vlan_id, name=vlan_name)
            elif len(parts) >= 5 and parts[3] == "l3-interface":
                l3_interface = parts[4]
                vlan_name = parts[2]
                l3_interfaces[vlan_name] = l3_interface

        # fill in the collected l3 information:
        for vlan in vlans_model.vlans.values():
            if l3_interfaces.get(vlan.name):
                vlan.layer3_interface = l3_interface
        self.model.vlans = vlans_model


def lldp_interface_builder(lldp_model: LLDP, line_parts: list[str]):
    """
    Construct the LLDPInterface model from parts for a given LLDP model.
    """
    lldp_interface_name = line_parts[4]
    if lldp_model.interfaces.get(lldp_interface_name) is None:
        lldp_model.interfaces[lldp_interface_name] = LLDPInterface(
            interface_name=lldp_interface_name, enabled=True
        )
    if len(line_parts) >= 6:
        if line_parts[5] == "disable":
            lldp_model.interfaces[lldp_interface_name].enabled = False
        else:
            feature = " ".join(line_parts[5::])
            if lldp_model.interfaces[lldp_interface_name].features is None:
                lldp_model.interfaces[lldp_interface_name].features = set()

            lldp_model.interfaces[lldp_interface_name].features.add(feature)
