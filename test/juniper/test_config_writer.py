from src.juniper.configbuilder import ConfigBuilder
import pytest
from src.juniper.token import *

def test_instantiate_config_builder(system_tokens):
    cb = ConfigBuilder(tokens = system_tokens["tokens"])
    

    assert isinstance(cb, ConfigBuilder)
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.IDENTIFIER, literal='system')
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.LEFT_CURLY, literal='{')
