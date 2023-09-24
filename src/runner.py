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
