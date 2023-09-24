from pydantic import BaseModel


class Lexer(BaseModel):
    source: str
    position: int = 0
    read_position: int = 0
    character: str = ""
