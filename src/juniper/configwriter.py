from pydantic import BaseModel
import logging
from .token import Token, TokenType
import string

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class Stanza(BaseModel):
    """
    Struct to keep track of the stanza as we work through the configuration.

    stanza_pointer: integer indicating the size of the stanza_stack
    stanza_stack_record: list of items where the item is a list of strings
     that represent a hierarchy in the Junos config
    stanza_stack: the current configuration statements in the stanza
    config_line_stack: list of strings that
    """

    stanza_pointer: int = 0
    stanza_stack_record: list[list[str]] = []
    stanza_stack: list[str] = []
    config_line_stack: list[str] = []
    inside_bracket_array: bool = False
    next_inactive: bool = False
    next_protect: bool = False


class ConfigWriter(BaseModel):
    """
    Turns a list of Tokens into a Juniper configuration
     in the 'set-style'.

    """

    tokens: list[Token]
    position: int = 0
    read_position: int = 0
    output: str = ""
    stanza: Stanza = Stanza()

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
                    LOGGER.info(
                        f"left curly start: {self.stanza.stanza_pointer}\n{self.stanza.stanza_stack_record}\n{self.stanza.stanza_stack}\n{self.stanza.config_line_stack}\n{self.stanza.stanza_stack_record}"
                    )
                    if self.stanza.next_inactive:
                        addition = build_string(
                            self.stanza.stanza_stack_record,
                            self.stanza.config_line_stack,
                        ).replace("set", "deactivate")
                        self.output += addition + "\n"
                        self.stanza.next_inactive = False
                    elif self.stanza.next_protect:
                        addition = build_string(
                            self.stanza.stanza_stack_record,
                            self.stanza.config_line_stack,
                        ).replace("set", "protect")
                        self.output += addition + "\n"
                        self.stanza.next_protect = False

                    self.stanza.stanza_pointer += 1
                    self.stanza.stanza_stack_record.append(
                        self.stanza.stanza_stack.copy()
                    )
                    self.stanza.stanza_stack.clear()
                    self.stanza.config_line_stack.clear()
                    LOGGER.info(
                        f"left curly end: {self.stanza.stanza_pointer}\n{self.stanza.stanza_stack_record}\n{self.stanza.stanza_stack}\n{self.stanza.config_line_stack}\n{self.stanza.stanza_stack_record}"
                    )

                case TokenType.RIGHT_CURLY:
                    LOGGER.info("right curly")
                    self.stanza.stanza_pointer -= 1
                    self.stanza.stanza_stack.clear()
                    self.stanza.stanza_stack_record.pop()
                    LOGGER.info(
                        f"right curly:\n{self.stanza.stanza_pointer}\n{self.stanza.stanza_stack_record}\n{self.stanza.stanza_stack}\n{self.stanza.config_line_stack}"
                    )

                case TokenType.LEFT_BRACKET:
                    LOGGER.info("left bracket")
                    self.stanza.inside_bracket_array = True

                case TokenType.RIGHT_BRACKET:
                    LOGGER.info("right bracket")
                    self.stanza.inside_bracket_array = False
                    self.stanza.config_line_stack.clear()

                case TokenType.IDENTIFIER:
                    statement = token.literal
                    LOGGER.info(f"identifier statement: {statement}")

                    if statement.endswith(";"):
                        self.stanza.config_line_stack.append(statement)
                        addition = build_string(
                            self.stanza.stanza_stack_record,
                            self.stanza.config_line_stack,
                        )
                        if self.stanza.next_inactive:
                            deactivate = addition.replace("set", "deactivate")
                            self.stanza.next_inactive = False
                            self.output += addition + "\n"
                            self.output += deactivate + "\n"
                        elif self.stanza.next_protect:
                            protect = addition.replace("set", "protect")
                            self.stanza.next_protect = False
                            self.output += addition + "\n"
                            self.output += protect + "\n"
                        else:
                            self.output += addition + "\n"
                        self.stanza.config_line_stack.clear()
                        self.stanza.stanza_stack.clear()
                    elif self.stanza.inside_bracket_array:
                        self.stanza.config_line_stack.append(statement)
                        addition = build_string(
                            self.stanza.stanza_stack_record,
                            self.stanza.config_line_stack,
                        )
                        self.stanza.config_line_stack.pop()
                        self.output += addition + "\n"
                    elif statement == "inactive:":
                        self.stanza.next_inactive = True
                    elif statement == "protect:":
                        self.stanza.next_protect = True
                    elif statement == "replace:":
                        pass  # not relevant
                    else:
                        LOGGER.debug(f"before: {self.stanza.stanza_stack}")
                        self.stanza.stanza_stack.append(statement)
                        self.stanza.config_line_stack.append(statement)
                        LOGGER.debug(f"after: {self.stanza.stanza_stack}")
                case TokenType.COMMENT:
                    LOGGER.info("comment")
                    # self.move_past_comment()
                    pass

                case TokenType.SEMICOLON:
                    LOGGER.info("caught SEMICOLON")

                    if (
                        self.tokens[self.read_position - 2].token_type
                        == TokenType.RIGHT_BRACKET
                    ):
                        # this means we have a lost ';' after iterating the values
                        # in brackets and we need to wipe the stanza_stack

                        self.stanza.stanza_stack.clear()

                    self.stanza.config_line_stack.clear()
                case TokenType.EOF:
                    LOGGER.info("caught EOF")

                    break

                case other:
                    LOGGER.error("did not catch it", token)
            LOGGER.debug(
                f"stanza_stack {self.stanza.stanza_stack}",
            )
            LOGGER.debug(f"stanza_pointer {self.stanza.stanza_pointer}")
            LOGGER.debug(f"stanza_stack_record {self.stanza.stanza_stack_record}")
            LOGGER.debug(f"config_line_stack {self.stanza.config_line_stack}")

    def build_set_config(self) -> str:
        self.read_tokens()

        return self.output.strip()

    def move_past_comment(self) -> None:
        """
        Process tokens after a pound indicated comment.

        This means that tokens following a pound will be ignored untill
        one of following tokens appear:
        - newline
        - RightSquirly ('}') Tokens
        - an identifier that can be interpreted as a terminating statment
        """
        LOGGER.debug(f"move_past_comment")
        while True:
            next_token = self.tokens[self.read_position]
            LOGGER.debug(f"move_past_comment: {next_token}")
            if (
                next_token.token_type == TokenType.NEWLINE
                or next_token.token_type == TokenType.RIGHT_CURLY
            ):
                break
            if next_token.token_type == TokenType.IDENTIFIER:
                statement = next_token.literal
                if statement.endswith(";"):
                    break

            self.position = self.read_position
            self.read_position += 1


def build_string(
    stanza_stack_record: list[list[str]], config_line_stack: list[str]
) -> str:
    new_string = "set"

    for vec in stanza_stack_record:
        for string in vec:
            new_string = new_string + " " + string

    for string in config_line_stack:
        new_string = new_string + " " + string

    if new_string.endswith(";"):
        new_string = new_string[:-1]

    return new_string
