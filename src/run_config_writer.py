# for every configuration file in test date, create a corresponding token file.
from juniper.configwriter import ConfigWriter
from juniper.lexer import Lexer
import glob
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
import json

"""
LOGGER = logging.getLogger(__name__)
PATH = Path(__file__)
TEST_DIR = PATH.parent.parent
ALL_TOKEN_FILES = glob.glob(str(TEST_DIR) + "/test/data/tokens/*.json")

for path in ALL_TOKEN_FILES[-2:-1]:
    print(f"NEW PATH {path}")
    with open(path, "rt") as f:
        tokens = f.read()
        tokens_d = json.loads(tokens)

    cb = ConfigWriter(tokens=tokens_d["tokens"])
    cb.read_tokens()
    print("output",cb.output)
"""
SOURCE = """system {
            host-name myrouter;
            services {
                ftp;
                ssh;
                telnet;
                netconf {
                    ssh;
                }
            }
        }
        """
lexer = Lexer(source=SOURCE)
lexer.read_tokens()
cb = ConfigWriter(tokens=lexer.tokens)
cb.read_tokens()
print("output:\n")
print(cb.output)


original = """policy-options {
    policy-statement directs {
        term Lo0 {
            from {
                protocol direct;
                route-filter 192.168.100.0/24 orlonger;
            }
            then accept;
        }
    }   
}"""

converted = """
set policy-options policy-statement directs term Lo0 from protocol direct
set policy-options policy-statement directs term Lo0 from route-filter 192.168.100.0/24 orlonger
set policy-options policy-statement directs term Lo0 then accept"""

lexer = Lexer(source=original)
lexer.read_tokens()
cb = ConfigWriter(tokens=lexer.tokens)
outcome = cb.build_set_config()
print(outcome)
print(converted)

assert outcome.strip() == converted.strip()
