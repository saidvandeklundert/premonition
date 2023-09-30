from pydantic import BaseModel, model_validator
import ipaddress
from typing import Literal
from enum import Enum
import yaml


class Action(str, Enum):
    DENY = "deny"
    PERMIT = "permit"


class Port(str, Enum):
    HTTPS = 443
    HTTP = 80
    DNS = 60


class Protocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"
    ANY = "any"


class Flow(BaseModel):
    """
    Description of an individual flow.

    This model is to be translated to and from Network device access-list
    configurations and ease analysis, unit testing, configuration building,
    and verification of applied access-lists.


    """

    ticket: str
    description: str
    source_network: ipaddress.IPv4Network | ipaddress.IPv6Network | Literal["any"]
    destination_network: ipaddress.IPv4Network | ipaddress.IPv6Network | Literal["any"]
    destination_port: int | Port | Literal["any"]
    source_port: int | Port | Literal["any"]
    source_zone: str | None = None
    protocol: str | Protocol
    action: Action
    destination_zone: str | None = None
    stateful: bool = False

    @model_validator(mode="after")
    def check_stateful_declaration(self):
        source_zone = self.source_zone
        destination_zone = self.destination_zone
        if source_zone is None and destination_zone is None:
            assert self.stateful is False

        else:
            assert self.stateful is True
            assert self.source_zone is self.destination_zone

        return self

    class Config:
        use_enum_values = True


class Filter(BaseModel):
    """
    Model representing an access-list on a device.

    The complete list of flows can represent an access-list or a firewall filter.
    """

    flows: list[Flow] = []


def main():
    acl = Filter(
        flows=[
            Flow(
                ticket="S-100",
                description="allow outboud HTTPS",
                source_network="any",
                destination_network="any",
                destination_port=Port.HTTPS,
                protocol=Protocol.TCP,
                action=Action.PERMIT,
                source_port="any",
            ),
            Flow(
                ticket="S-101",
                description="allow outbound DNS",
                source_network="20.0.0.0/24",
                destination_network="8.8.8.8/32",
                destination_port=Port.DNS,
                protocol=Protocol.UDP,
                action=Action.PERMIT,
                source_port="any",
            ),
            Flow(
                ticket="S-1",
                description="deny all",
                source_network="any",
                destination_network="any",
                destination_port="any",
                protocol=Protocol.ANY,
                action=Action.DENY,
                source_port="any",
            ),
        ]
    )

    print(acl.model_dump_json(indent=4))
    d = acl.model_dump()
    print(yaml.dump(d))
