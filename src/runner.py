from pprint import pprint
from models.device import JuniperDevice

lldp_config = """set protocols lldp port-description-type interface-description
set protocols lldp interface all
set protocols lldp interface me0 disable
"""
device = JuniperDevice(hostname="r1", configuration=lldp_config)
device.build_models()
print(device.model_dump_json(indent=2, exclude="configuration"))
