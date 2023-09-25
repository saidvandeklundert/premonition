from pydantic import BaseModel
import logging
from .token import Token, TokenType
import string

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


class ConfigWriter(BaseModel):
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
        """
        Move through the list of Tokens and build the configuration.
        """
        while self.current_token.token_type != TokenType.EOF:
            self.read_token()
            token = self.current_token
            match token.token_type:
                case TokenType.LEFT_CURLY:
                    LOGGER.info("left curly")
                case TokenType.RIGHT_CURLY:
                    LOGGER.info("right curly")
                case TokenType.LEFT_BRACKET:
                    LOGGER.info("left bracket")
                case TokenType.RIGHT_BRACKET:
                    LOGGER.info("right bracket")
                case TokenType.RIGHT_BRACKET:
                    LOGGER.info("right bracket")
                case TokenType.IDENTIFIER:
                    LOGGER.info("identifier")
                case TokenType.COMMENT:
                    LOGGER.info("comment")
                case TokenType.EOF:
                    LOGGER.info("caught EOF")
                    break
                case other:
                    LOGGER.error("did not catch it", token)
