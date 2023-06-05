from models.token import Token
from util.token_types import TokenTypes


class LexicalInformation:
    def __init__(self):
        self.lexeme_builder = ""
        self.line = 0
        self.column = 0

    def clean(self):
        self.lexeme_builder = ""
        self.column = 0
        self.line = 0

    def write_char(self, character: str) -> None:
        if not (self.lexeme_builder == "" and character.isspace()):
            self.lexeme_builder += character

    def gen_token(self, token_type: TokenTypes) -> Token:
        new_token = Token(self.lexeme_builder, line_number=self.line, column=self.column, token_type=token_type)
        line = self.line
        self.clean()
        self.line = line
        return new_token

    def has_ongoing_token(self) -> bool:
        return self.lexeme_builder != ""
