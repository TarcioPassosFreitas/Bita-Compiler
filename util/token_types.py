from enum import Enum


class TokenTypes(Enum):
    IDENTIFIER = 1
    OPERATOR = 2
    NUMBER = 3
    BOOLEAN = 4
    STRING = 5
    RESERVED = 6
    DELIMITER = 7
    COMMENT = 8
