from pydantic import BaseModel
import logging
from .token import Token, TokenType
import string

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class ConfigBuilder(BaseModel):
    """
    Turns a list of Tokens into a Juniper configuration
     in the 'set-style'.

    """

    tokens: list[Token]
    position: int = 0
    read_position: int = 0
    output: str = ""

    @property
    def current_token(self) -> Token:
        return self.tokens[self.position]

    def read_token(self) -> None:
        """
        Advance the pointer to the next token and update the token
        that is under evaluation.
        """
        self.position = self.read_position
        self.read_position += 1

    def read_tokens(self) -> None:
        while self.current_token.token_type != TokenType.EOF:
            self.read_token()
            print(self.current_token)
