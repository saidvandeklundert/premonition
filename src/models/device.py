from pydantic import BaseModel
from .protocols.lldp import LLDP, LLDPInterface
from juniper.lexer import Lexer
from juniper.configwriter import ConfigWriter

class DeviceModel(BaseModel):
    """
    Vendor agnostic representation of a network node.
    """
    lldp:LLDP |None = None
class Device(BaseModel):
    """
    Model of a device
    """

    hostname:str
    configuration: str
    model:DeviceModel =DeviceModel()

    def show_model(self):
        return self.model_dump_json(indent=4,exclude="configuration")

class JuniperDevice(Device):
    """
    Variant specific for Juniper devices.
    """
    configuration_set_style :str|None = None


    def show_model(self):
        return self.model_dump(exclude="configuration,configuration_set_style",exclude_defaults=True)
    
    def show_model_json(self):
        return self.model_dump_json(indent=4,exclude="configuration,configuration_set_style")
    
    def build_models(self) -> None:
        """
        Build the models from the device configuration.
        """
        lexer = Lexer(source=self.configuration)
        lexer.read_tokens()
        cw = ConfigWriter(tokens=lexer.tokens)
        self.configuration_set_style= cw.build_set_config()
        lldp_model = self.lldp_builder()

        self.model.lldp = lldp_model

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
                lldp_model.interfaces[lldp_interface_name].features= set()
            
  
            lldp_model.interfaces[lldp_interface_name].features.add(feature)
