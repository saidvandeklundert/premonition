from pydantic import BaseModel
import ipaddress


class Syslog(BaseModel):
    servers: list[ipaddress.IPv4Address | ipaddress.IPv6Address] = []


class NameServers(BaseModel):
    servers: list[ipaddress.IPv4Address | ipaddress.IPv6Address] = []


class System(BaseModel):
    """
    Model that describes the system settings of the device.
    """

    syslog: Syslog = Syslog()
    name_servers: NameServers = NameServers()
