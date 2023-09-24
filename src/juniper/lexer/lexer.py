from pydantic import BaseModel
import logging
from .token import Token, TokenType
from typing import List

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class Lexer(BaseModel):
    source: str
    position: int = 0
    read_position: int = 0
    character: str = " "
    tokens: list[Token] = []

    @property
    def end(self) -> int:
        return len(self.source)

    def read_char(self) -> None:
        """
        Read the character at the current position and move the read_position
        """
        if self.read_position >= self.end:
            self.character = "end"
        else:
            self.character = self.source[self.read_position]
            LOGGER.debug(self.character)
        self.position = self.read_position

        self.read_position += 1

    def skip_whitespace(self) -> None:
        while self.character in [" ", "\t", "\n", "\r"]:
            LOGGER.debug("skip white space")
            self.read_char()

    def next_token(self) -> None:
        self.skip_whitespace()
        character = self.character
        LOGGER.debug(f"assigning token to: {character}")

        match character:
            case "{":
                tok = Token(token_type=TokenType.LEFT_CURLY, literal=character)

            case _:
                if True is False:
                    pass
                else:
                    tok = Token(token_type=TokenType.UNKNOWN, literal=character)

        self.tokens.append(tok)

        self.read_char()
