from util.token_types import TokenTypes


class Token:
    def __init__(self, lexeme: str, line_number: int, token_type: TokenTypes, column: int = 0):
        self.line_number = line_number
        self.column = column
        self.__token_type = token_type
        self.__lexeme = lexeme

    def __str__(self):
        return f"{self.__lexeme}"

    def __repr__(self):
        return self.__str__()

    def get_lexeme(self):
        return self.__lexeme

    def get_token_type(self):
        return self.__token_type
