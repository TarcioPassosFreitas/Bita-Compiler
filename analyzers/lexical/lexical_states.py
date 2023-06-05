from enum import Enum


class LexicalStates(Enum):
    NIL = 0
    STRING = 1
    IDENTIFIER = 2
    NUMBER = 3
    OPERATOR = 4
    LINE_COMMENT = 5
    BLOCK_COMMENT = 6
