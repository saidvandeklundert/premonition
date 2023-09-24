# ipython -i .\src\runner.py
from juniper.lexer.lexer import Lexer

lexer = Lexer(source="  start")
lexer.read_char()
lexer.skip_whitespace()


lexer = Lexer(source="{")
lexer.next_token()
