from models.token import Token
from analyzers.syntactic import sp_start
from util.data_structure.queue import Queue
from util.token_types import TokenTypes
from analyzers.lexical import LexicalAnalyzer


def execute():
    error_list = []
    lista_tokens = [

        # Token('start', 1, TokenTypes.RESERVED),
        # Token('{', 1, TokenTypes.RESERVED),
        # Token('var', 1, TokenTypes.RESERVED),
        # Token('{', 1, TokenTypes.RESERVED),
        # Token('int', 1, TokenTypes.RESERVED),
        # Token('a', 1, TokenTypes.IDENTIFIER),
        # Token('=', 1, TokenTypes.OPERATOR),
        # Token('2', 1, TokenTypes.NUMBER),
        # Token(';', 1, TokenTypes.RESERVED),
        # Token('}', 1, TokenTypes.RESERVED),
        # Token('}', 1, TokenTypes.RESERVED),

        # Token('const', 1, TokenTypes.RESERVED),
        # Token('{', 1, TokenTypes.RESERVED),
        # Token('real', 2, TokenTypes.RESERVED),
        # Token('c', 2, TokenTypes.IDENTIFIER),
        # Token('=', 2, TokenTypes.OPERATOR),
        # Token('1.5', 2, TokenTypes.NUMBER),
        # Token(';', 2, TokenTypes.RESERVED),
        # Token('}', 3, TokenTypes.RESERVED),
        # Token('start', 4, TokenTypes.RESERVED),
        # Token('{', 4, TokenTypes.RESERVED),
        # Token('var', 5, TokenTypes.RESERVED),
        # Token('{', 5, TokenTypes.RESERVED),
        # Token('int', 6, TokenTypes.RESERVED),
        # Token('a', 6, TokenTypes.IDENTIFIER),
        # Token('=', 6, TokenTypes.OPERATOR),
        # Token('3', 6, TokenTypes.NUMBER),
        # Token(';', 6, TokenTypes.RESERVED),
        # Token('}', 7, TokenTypes.RESERVED),
        # Token('}', 8, TokenTypes.RESERVED),

        # Token('function', 1, TokenTypes.RESERVED),
        # Token('real', 1, TokenTypes.RESERVED),
        # Token('calculateArea', 1, TokenTypes.IDENTIFIER),
        # Token('(', 1, TokenTypes.RESERVED),
        # Token('int', 1, TokenTypes.RESERVED),
        # Token('width', 1, TokenTypes.IDENTIFIER),
        # Token(',', 1, TokenTypes.RESERVED),
        # Token('int', 1, TokenTypes.RESERVED),
        # Token('height', 1, TokenTypes.IDENTIFIER),
        # Token(')', 1, TokenTypes.RESERVED),
        # Token('{', 2, TokenTypes.RESERVED),
        # Token('var', 3, TokenTypes.RESERVED),
        # Token('{', 3, TokenTypes.RESERVED),
        # Token('real', 4, TokenTypes.RESERVED),
        # Token('area', 4, TokenTypes.IDENTIFIER),
        # Token(';', 4, TokenTypes.RESERVED),
        # Token('}', 5, TokenTypes.RESERVED),
        # Token('area', 6, TokenTypes.IDENTIFIER),
        # Token('=', 6, TokenTypes.OPERATOR),
        # Token('width', 6, TokenTypes.IDENTIFIER),
        # Token('*', 6, TokenTypes.OPERATOR),
        # Token('height', 6, TokenTypes.IDENTIFIER),
        # Token(';', 6, TokenTypes.RESERVED),
        # Token('return', 8, TokenTypes.RESERVED),
        # Token('area', 8, TokenTypes.IDENTIFIER),
        # Token(';', 8, TokenTypes.RESERVED),
        # Token('}', 9, TokenTypes.RESERVED),
        # Token('start', 10, TokenTypes.RESERVED),
        # Token('{', 10, TokenTypes.RESERVED),
        # Token('calculateArea', 11, TokenTypes.IDENTIFIER),
        # Token('(', 11, TokenTypes.RESERVED),
        # Token('2', 11, TokenTypes.NUMBER),
        # Token(',', 11, TokenTypes.RESERVED),
        # Token('3', 11, TokenTypes.NUMBER),
        # Token(')', 11, TokenTypes.RESERVED),
        # Token(';', 11, TokenTypes.RESERVED),
        # Token('}', 12, TokenTypes.RESERVED)

        # Token('start', 1, TokenTypes.RESERVED),
        # Token('{', 2, TokenTypes.DELIMITER),
        # Token('if', 3, TokenTypes.RESERVED),
        # Token('(', 3, TokenTypes.DELIMITER),
        # Token('a', 3, TokenTypes.IDENTIFIER),
        # Token('==', 3, TokenTypes.OPERATOR),
        # Token('3', 3, TokenTypes.NUMBER),
        # Token(')', 3, TokenTypes.DELIMITER),
        # Token('then', 3, TokenTypes.RESERVED),
        # Token('{', 4, TokenTypes.DELIMITER),
        # Token('b', 5, TokenTypes.IDENTIFIER),
        # Token('=', 5, TokenTypes.OPERATOR),
        # Token('c', 5, TokenTypes.IDENTIFIER),
        # Token(';', 5, TokenTypes.DELIMITER),
        # Token('}', 6, TokenTypes.DELIMITER),
        # Token('}', 7, TokenTypes.DELIMITER),

        # Token('start', 1, TokenTypes.RESERVED),
        # Token('{', 2, TokenTypes.DELIMITER),
        # Token('var', 3, TokenTypes.RESERVED),
        # Token('{', 4, TokenTypes.DELIMITER),
        # Token('int', 5, TokenTypes.RESERVED),
        # Token('a', 5, TokenTypes.IDENTIFIER),
        # Token('[', 5, TokenTypes.DELIMITER),
        # Token('1', 5, TokenTypes.NUMBER),
        # Token(']', 5, TokenTypes.DELIMITER),
        # Token(';', 5, TokenTypes.DELIMITER),
        # Token('}', 6, TokenTypes.DELIMITER),
        # Token('a', 7, TokenTypes.IDENTIFIER),
        # Token('[', 7, TokenTypes.DELIMITER),
        # Token('0', 7, TokenTypes.NUMBER),
        # Token(']', 7, TokenTypes.DELIMITER),
        # Token('=', 7, TokenTypes.OPERATOR),
        # Token('10', 7, TokenTypes.NUMBER),
        # Token(';', 7, TokenTypes.DELIMITER),
        # Token('}', 8, TokenTypes.DELIMITER)

        # Token('struct', 1, TokenTypes.RESERVED),
        # Token('teste', 1, TokenTypes.IDENTIFIER),
        # Token('{', 2, TokenTypes.DELIMITER),
        # Token('string', 3, TokenTypes.RESERVED),
        # Token('a', 3, TokenTypes.IDENTIFIER),
        # Token(';', 3, TokenTypes.DELIMITER),
        # Token('}', 4, TokenTypes.DELIMITER),
        # Token('start', 5, TokenTypes.RESERVED),
        # Token('{', 6, TokenTypes.DELIMITER),
        # Token('teste', 7, TokenTypes.IDENTIFIER),
        # Token('.', 7, TokenTypes.DELIMITER),
        # Token('a', 7, TokenTypes.IDENTIFIER),
        # Token('=', 7, TokenTypes.OPERATOR),
        # Token('3', 7, TokenTypes.NUMBER),
        # Token(';', 7, TokenTypes.DELIMITER),
        # Token('}', 8, TokenTypes.DELIMITER)

    ]
    sp_start(Queue(lista_tokens), error_list)  # Press Ctrl+F8 to toggle the breakpoint.
    if len(error_list) == 0:
        print("Não tem erros")
    else:
        print(error_list)


def main():
    parser = LexicalAnalyzer()
    with open('input.bita', 'r') as file:
        file_content = file.read()
        token_list = parser.start(tuple([character for character in file_content]))
        error_list = parser.errors

        sp_start(Queue(token_list), error_list)  # Press Ctrl+F8 to toggle the breakpoint.
        if len(error_list) == 0:
            print("Não tem erros")
        else:
            print(error_list)


if __name__ == '__main__':
    main()
