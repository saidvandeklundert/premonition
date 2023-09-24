from __future__ import annotations
from enum import Enum
from pydantic import BaseModel


class TokenType(str, Enum):
    IDENTIFIER = "IDENTIFIER"
    COMMENT = "COMMENT"
    EOF = "EOF"
    LEFT_CURLY = "{"
    RIGHT_CURLY = "}"
    SEMICOLON = ";"
    UNKNOWN = "UNKNOWN"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    POUND = "#"
    NEWLINE = "\n"


class Token(BaseModel):
    """
    The way a token is represented by our Lexer.
    """

    token_type: TokenType
    literal: str
