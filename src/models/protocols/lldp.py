from pydantic import BaseModel


class LLDPInterface(BaseModel):
    """
    The LLDP configuraion for a single interface.
    """

    interface_name: str
    enabled: bool = True
    features: set = set()


class LLDP(BaseModel):
    """
    The device LLDP settings.
    """

    config: str
    features: set = set()
    interfaces: dict[str, LLDPInterface] = {}

    def __iter__(self):
        return iter(self.interfaces.values())
