from pydantic import BaseModel


class Vlan(BaseModel):
    """
    Model that represents a single Vlan
    """

    features: set = set()
    vlan_id: int
    name: str | None = None
    description: str | None = None
    layer3_interface: str | None = None


class Vlans(BaseModel):
    """
    Model that represents the Vlans that are configured on the device.
    """

    features: set = set()
    vlans: dict[int, Vlan] = {}

    def __getitem__(self, item):
        return self.vlans.get(item)
