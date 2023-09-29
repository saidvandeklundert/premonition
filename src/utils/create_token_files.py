# for every configuration file in test date, create a corresponding token file.
from juniper.lexer import Lexer
import glob
from pathlib import Path

PATH = Path(__file__)
TEST_DIR = PATH.parent.parent
ALL_CONFIGURATION_FILES = glob.glob(str(TEST_DIR) + "/test/data/configurations/*.txt")
SET_CONFIGURATIONS = [
    filepath for filepath in ALL_CONFIGURATION_FILES if "set" in filepath
]
REGULAR_CONFIGURATIONS = [
    filepath for filepath in ALL_CONFIGURATION_FILES if "set" not in filepath
]

for path in REGULAR_CONFIGURATIONS:
    with open(path, "rt") as f:
        configuration = f.read()
    lexer = Lexer(source=configuration)
    lexer.read_tokens()
    tokens_json = lexer.tokens_json()

    with open(
        path.replace("txt", "json").replace("configurations", "tokens"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(tokens_json)
