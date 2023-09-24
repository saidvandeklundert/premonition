import glob

from pathlib import Path
import pytest
PATH = Path(__file__)
TEST_DIR = PATH.parent

ALL_CONFIGURATION_FILES = glob.glob(str(TEST_DIR) + "/data/configurations/*.txt")
SET_CONFIGURATIONS = [filepath for filepath in ALL_CONFIGURATION_FILES if "set" in filepath]
REGULAR_CONFIGURATIONS = [filepath for filepath in ALL_CONFIGURATION_FILES if "set" not in filepath]

@pytest.fixture(scope="session", autouse=True)
def configurations()->list[str]:
    configurations= []
    for path in ALL_CONFIGURATION_FILES:
        with open(path,"rt") as f:
            configuration = f.read()
            configurations.append(configuration)
    return configurations

@pytest.fixture(scope="session", autouse=True)
def configurations_regular()->list[str]:
    configurations= []
    for path in REGULAR_CONFIGURATIONS:
        with open(path,"rt") as f:
            configuration = f.read()
            configurations.append(configuration)
    return configurations

@pytest.fixture(scope="session", autouse=True)
def configurations_set()->list[str]:
    configurations= []
    for path in SET_CONFIGURATIONS:
        with open(path,"rt") as f:
            configuration = f.read()
            configurations.append(configuration)
    return configurations
        

#import pdb
#pdb.set_trace()