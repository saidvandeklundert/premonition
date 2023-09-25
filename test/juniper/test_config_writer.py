from src.juniper.configwriter import ConfigWriter
import pytest
from src.juniper.token import *

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

    