from pydantic import BaseModel
import logging
from .token import Token, TokenType
import string

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

WHITESPACES = {" ", "\t", "\n", "\r"}


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
        while self.character in WHITESPACES:
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
            case "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z":
                identifier = self.read_identifier()
                tok = Token(token_type=TokenType.IDENTIFIER, literal=identifier)
            case "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z":
                identifier = self.read_identifier()
                tok = Token(token_type=TokenType.IDENTIFIER, literal=identifier)
            case ":" | '"' | "-" | "_" | "^" | "<" | ">" | "*" | "." | "\\" | "/":  # | ";"
                identifier = self.read_identifier()
                tok = Token(token_type=TokenType.IDENTIFIER, literal=identifier)
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
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
            case "end":
                tok = Token(token_type=TokenType.EOF, literal="EOF")
            case _:
                LOGGER.error(f"unkown token: {character}")
                tok = Token(token_type=TokenType.UNKNOWN, literal=character)

        self.tokens.append(tok)

        self.read_char()

    def read_identifier(self) -> str:
        """
        Reads an identifier from the Juniper configuration.
        """
        position = self.position
        if self.character == '"':
            self.read_char()
            while self.character != '"':
                self.read_char()

        while self.character:
            self.read_char()
            if self.character in {
                " ",
                "\n",
                "end",
                "\t",
            }:
                break

        return self.source[position : self.position]

    def read_comment(self) -> str:
        """
        Reads a comment from the Juniper configuration.
        """
        position = self.position

        while self.character:
            self.read_char()
            if self.character in {"\n"}:
                break
        return self.source[position : self.position]

    def read_tokens(self) -> None:
        """
        Read all tokens from the provided source.
        """
        while self.character != "end":
            self.next_token()
        if self.tokens[-1].token_type != TokenType.EOF:
            self.tokens.append(Token(token_type=TokenType.EOF, literal="EOF"))

    def tokens_json(self) -> str:
        """
        Returns the tokens as JSON, excluding all other fields.
        """

        return self.model_dump_json(
            exclude="source,character,read_position,position", indent=4
        )

    def peek(self) -> str:
        """
        Peek ahead and return the next char.
        """
        return self.tokens[self.read_position]
