import glob
import json
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
        


@pytest.fixture()
def system_tokens():
    """
    Returns the JSON that represents a list of tokens that describe a small set of the 
    systems configuration.
    """
    token_list = '{"tokens":[{"token_type":"IDENTIFIER","literal":"system"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"host-name"},{"token_type":"IDENTIFIER","literal":"myrouter;"},{"token_type":"IDENTIFIER","literal":"services"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"ftp;"},{"token_type":"IDENTIFIER","literal":"ssh;"},{"token_type":"IDENTIFIER","literal":"telnet;"},{"token_type":"IDENTIFIER","literal":"netconf"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"ssh;"},{"token_type":"}","literal":"}"},{"token_type":"}","literal":"}"},{"token_type":"}","literal":"}"},{"token_type":"EOF","literal":"EOF"}]}'

    d = json.loads(token_list)
    return d