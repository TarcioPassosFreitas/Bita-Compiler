from enum import Enum


class CommentType(Enum):
    LINE = 0
    BLOCK = 1


class Terminals:
    def __init__(self):
        self.reserved_words = (
            "var", "const", "struct", "procedure", "function",
            "start", "return", "if", "else", "then", "while", "read",
            "print", "int", "real", "boolean", "string", "true",
            "false"
        )
        self.arithmetic_operators = (
            "+", "-", "*", "/", "++", "--"
        )
        self.relational_operators = (
            "!=", "==", "<", "<=", ">", ">=", "="
        )
        self.logical_operators = (
            "!", "&&", "||"
        )
        self.delimiters = (
            ";", ",", "(", ")", "[", "]", "{", "}", "."
        )
        self.comments: dict[CommentType, tuple[str]] = {
            CommentType.LINE: tuple(["//"]),
            CommentType.BLOCK: ("/*", "*/")
        }

    @property
    def operators(self) -> tuple[str]:
        all_operators = self.arithmetic_operators + self.relational_operators + self.logical_operators
        return tuple(all_operators)

    def is_reserved(self, element: str) -> bool:
        return element in self.reserved_words
