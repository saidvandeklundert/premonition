from rich import print
from premonition import JuniperDevice
from original import original

dev = JuniperDevice(hostname="r1", configuration=original)
dev.build_models()
print(dev.model_dump_json(indent=2, exclude="configuration"))
