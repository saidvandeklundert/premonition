from src.juniper.lexer.lexer import Lexer

def test_instantiate_lexer():
    lexer = Lexer(source="some text to lex")

    
    assert isinstance(lexer, Lexer)
