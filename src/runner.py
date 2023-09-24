# ipython -i .\src\runner.py
from juniper.lexer.lexer import Lexer

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


for val in lexer.tokens:
    print(val.literal)
