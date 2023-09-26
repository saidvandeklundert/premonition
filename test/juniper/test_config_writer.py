from src.juniper.configwriter import ConfigWriter
import pytest
from src.juniper.token import *
from src.juniper.lexer import Lexer

from test.conftest import REGULAR_CONFIGURATIONS, SET_CONFIGURATIONS

def test_instantiate_config_builder(system_tokens):
    cb = ConfigWriter(tokens = system_tokens["tokens"])
    

    assert isinstance(cb, ConfigWriter)
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.IDENTIFIER, literal='system')
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.LEFT_CURLY, literal='{')


def test_load_all_token_files(all_tokens_from_files):
    for tokens in all_tokens_from_files:
        cb = ConfigWriter(tokens = tokens["tokens"])
        cb.read_tokens()

paramatrized = [(path) for path in REGULAR_CONFIGURATIONS]

@pytest.mark.parametrize(
    "path",
    paramatrized,
)
def test_configuration(path):
    
    set_config, expected_config = helper_return_set_config_expected_config(path)
    assert set_config ==  expected_config


def helper_return_set_config_expected_config(path:str)->tuple[str,str]:
    """
    Take a path to a regular configuration, then convert it to the 'set-style'

    Open the expected 'set-style' configuration.

    Return both as a tuple.
    """
    with open(path, "rt") as f:
        original = f.read()
    lexer = Lexer(source=original)
    lexer.read_tokens()
    
    cb = ConfigWriter(tokens=lexer.tokens)
    set_config = cb.build_set_config()
    with open(path.replace(".txt","_set.txt"), "rt") as f:
        expected_config = f.read()    
    return set_config, expected_config   