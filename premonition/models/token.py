from __future__ import annotations
from pydantic import BaseModel
from enum import Enum


class TokenType(str, Enum):
    START = "START"
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

    def __str__(self):
        return f"TokenType.{self.name}"

    def __repr__(self):
        return f"TokenType.{self.name}"


class Token(BaseModel):
    """
    The way a token is represented by our Lexer.
    """

    token_type: TokenType
    literal: str

    def __str__(self):
        return f'Token(token_type={self.token_type}, literal="{self.literal}")'

    def __repr__(self):
        return f'Token(token_type={self.token_type}, literal="{self.literal}")'
