from src.juniper.lexer import Lexer
from src.juniper.token import TokenType, Token
import pytest
from test.conftest import REGULAR_CONFIGURATIONS
import json

SOURCE_1  ="""system {
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
SOURCE_1_LIST = ["system", "{", "host-name", "myrouter;", "services", "{", "ftp;", "ssh;", "telnet;", "netconf", "{", "ssh;", "}", "}", "}", "EOF"]

SOURCE_2 = """system {
    root-authentication {
        encrypted-password "$COMPLEXTHASH_)(*@#(&%*)(@#*&%))"; ## SECRET-DATA
    }
}"""

SOURCE_2_LIST = [
    "system", "{", "root-authentication", "{", "encrypted-password", '"$COMPLEXTHASH_)(*@#(&%*)(@#*&%))";', "## SECRET-DATA", "}", "}", "EOF"]

def test_instantiate_lexer():
    lexer = Lexer(source="some text to lex")
    
    assert isinstance(lexer, Lexer)

def test_instantiate_lexer():
    
    lexer = Lexer(source="some text to lex")
    
    
    
    lexer.read_tokens()
    tokens_json = lexer.tokens_json()

    assert isinstance(tokens_json,str)

    d = json.loads(tokens_json)
    token = Token(**d["tokens"][0])
    assert isinstance(token,Token)


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


@pytest.mark.parametrize(
    "source, expected",
    [
        ("  an_identifier and_another_one", ["an_identifier", "and_another_one", "EOF"]),
        ('  "*879623542@@p" "@#$llaklk"', ['"*879623542@@p"', '"@#$llaklk"', "EOF"]),
        ('  word1 word2\nword3\tword4\t\t\t\nword5', ["word1","word2","word3","word4","word5", "EOF"]),
        (SOURCE_1, SOURCE_1_LIST),     
        (SOURCE_2, SOURCE_2_LIST),     
    ],
)
def test_lexer_read_identifier(source, expected):
    """
    Verify the lexer can read the expected identifiers.
    """
    lexer = Lexer(source=source)
    lexer.read_tokens()
    
    read_identifiers = []
    for token in lexer.tokens:
        read_identifiers.append(token.literal)
    assert read_identifiers == expected, f"Did not read all the expected identifiers:\nGot:{read_identifiers}\nExpected:{expected}"
  

@pytest.mark.parametrize(
    "path",
    [ (path) for path in REGULAR_CONFIGURATIONS],
)
def test_lexer_all_regular_configurations(path):
    """
    Verify the lexer can read the expected identifiers.

    Also verifies every token stream ends with an EOF.
    """
    with open(path,"rt") as f:
        configuration = f.read()
    
    lexer = Lexer(source=configuration)
    lexer.read_tokens()
    
    assert len(lexer.tokens) >1
    assert lexer.tokens[-1].token_type == TokenType.EOF

