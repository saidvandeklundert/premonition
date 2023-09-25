# ipython -i .\src\runner.py
from juniper.lexer import Lexer
from juniper.configbuilder import ConfigBuilder

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


cb = ConfigBuilder(tokens=lexer.tokens)

cb.read_tokens()
import json

token_list = '{"tokens":[{"token_type":"IDENTIFIER","literal":"system"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"host-name"},{"token_type":"IDENTIFIER","literal":"myrouter;"},{"token_type":"IDENTIFIER","literal":"services"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"ftp;"},{"token_type":"IDENTIFIER","literal":"ssh;"},{"token_type":"IDENTIFIER","literal":"telnet;"},{"token_type":"IDENTIFIER","literal":"netconf"},{"token_type":"{","literal":"{"},{"token_type":"IDENTIFIER","literal":"ssh;"},{"token_type":"}","literal":"}"},{"token_type":"}","literal":"}"},{"token_type":"}","literal":"}"},{"token_type":"EOF","literal":"EOF"}]}'

d = json.loads(token_list)

cb = ConfigBuilder(tokens=d["tokens"])
