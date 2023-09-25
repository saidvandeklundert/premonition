# for every configuration file in test date, create a corresponding token file.
from src.juniper.configwriter import ConfigBuilder
import glob
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
import json

LOGGER = logging.getLogger(__name__)
PATH = Path(__file__)
TEST_DIR = PATH.parent.parent
ALL_TOKEN_FILES = glob.glob(str(TEST_DIR) + "/test/data/tokens/*.json")

for path in ALL_TOKEN_FILES:
    print(f"NEW PATH {path}")
    with open(path, "rt") as f:
        tokens = f.read()
        tokens_d = json.loads(tokens)

    cb = ConfigBuilder(tokens=tokens_d["tokens"])
    cb.read_tokens()
