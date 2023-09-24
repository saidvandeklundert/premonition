from pydantic import BaseModel
import logging
from .token import Token, TokenType
import string

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def all_identifier_start_characters() -> set[str]:
    """
    Returns a set of all characters that could signal the start of an identifier in
    Juniper configuration statements.
    """
    identifier_start = [x for x in string.ascii_lowercase]
    identifier_start.extend([x for x in string.ascii_uppercase])
    identifier_start.extend([":", '"', "-", "_", "^", "<", ">", "*", ".", "\\", "/"])
    return set(identifier_start)


IDENTIFIER_START = all_identifier_start_characters()


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
        """
        Skip all characters that contain whitespaces.
        """
        while self.character in [" ", "\t", "\n", "\r"]:
            LOGGER.debug("skip white space")
            self.read_char()

    def next_token(self) -> None:
        """
        Read the next token and add it to the list of tokens kept by the Lexer.
        """
        self.skip_whitespace()
        character = self.character
        LOGGER.debug(f"assigning token to: {character}")

        match character:
            case "end":
                tok = Token(token_type=TokenType.EOF, literal="EOF")
            case character if character in IDENTIFIER_START:
                identifier = self.read_identifier()
                tok = Token(token_type=TokenType.IDENTIFIER, literal=identifier)
            case "{":
                tok = Token(token_type=TokenType.LEFT_CURLY, literal=character)
            case "}":
                tok = Token(token_type=TokenType.RIGHT_CURLY, literal=character)
            case ";":
                tok = Token(token_type=TokenType.SEMICOLON, literal=character)
            case "[":
                tok = Token(token_type=TokenType.LEFT_BRACKET, literal=character)

            case "]":
                tok = Token(token_type=TokenType.RIGHT_BRACKET, literal=character)

            case "#":
                identifier = self.read_comment()
                tok = Token(token_type=TokenType.COMMENT, literal=identifier)

            case "\n":
                tok = Token(token_type=TokenType.NEWLINE, literal=character)

            case _:
                if True is False:
                    pass
                else:
                    LOGGER.warning(f"unkown token: {character}")
                    tok = Token(token_type=TokenType.UNKNOWN, literal=character)

        self.tokens.append(tok)

        self.read_char()

    def read_identifier(self) -> str:
        """
        Reads an identifier from the Juniper configuration.
        """
        position = self.position

        while self.character:
            self.read_char()
            if self.character in [" ", "end", "\n", "\t"]:
                break
        return self.source[position : self.position]

    def read_comment(self) -> str:
        """
        Reads a comment from the Juniper configuration.
        """
        position = self.position

        while self.character:
            self.read_char()
            if self.character in ["\n"]:
                break
        return self.source[position : self.position]

    def read_tokens(self) -> None:
        """
        Read all tokens from the provided source.
        """
        while self.character != "end":
            self.next_token()
