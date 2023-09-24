from src.juniper.configbuilder import ConfigBuilder
import pytest
from src.juniper.token import *

def test_instantiate_config_builder():
    cb = ConfigBuilder(
        tokens=[
            Token(token_type=TokenType.IDENTIFIER, literal='system'),
              Token(token_type=TokenType.EOF, literal='EOF')]
              )
    
    assert isinstance(cb, ConfigBuilder)
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.IDENTIFIER, literal='system')
    cb.read_token()
    assert cb.current_token == Token(token_type=TokenType.EOF, literal='EOF')
