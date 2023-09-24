from src.juniper.lexer.lexer import Lexer
from src.juniper.lexer.token import TokenType
import pytest


def test_instantiate_lexer():
    lexer = Lexer(source="some text to lex")
    
    assert isinstance(lexer, Lexer)


def test_lexer_read_char():
    lexer = Lexer(source="end")
    lexer.read_char()
    assert lexer.character == "e"
    assert lexer.position == 0
    assert lexer.read_position == 1
    lexer.read_char()
    assert lexer.character == "n"
    assert lexer.position == 1
    assert lexer.read_position == 2    
    lexer.read_char()
    assert lexer.character == "d"
    assert lexer.position == 2
    assert lexer.read_position == 3    
    lexer.read_char()
    assert lexer.character == "end"
    assert lexer.position == 3
    assert lexer.read_position == 4 



def test_lexer_skip_white_space():
    """
    Verify we skip all whitespaces and 
    end up with the char 's'
    """
    lexer = Lexer(source="  \t\n   start")
    
    lexer.skip_whitespace()
    
    assert lexer.character == "s"

def test_lexer_read_single_token():
    """
    Read a single token
    """
    lexer = Lexer(source="{")
    lexer.next_token()
    
    assert lexer.tokens[0].token_type == TokenType.LEFT_CURLY