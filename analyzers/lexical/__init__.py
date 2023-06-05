from analyzers.lexical.lexical_information import LexicalInformation
from analyzers.lexical.lexical_states import LexicalStates
from models.terminals import Terminals, CommentType
from models.token import Token
from util.token_types import TokenTypes


def _is_line_break(character: str, previous_character: str) -> bool:
    return character == '\n' or previous_character + character == '\r\n'


def _is_valid_symbol(character: str) -> bool:
    return (character.isalnum() or character == "_") or character.isspace()


class LexicalAnalyzer:
    def __init__(self):
        self.__terminals = Terminals()
        self._state = LexicalStates.NIL
        self.__state_memory: bool = False
        self._state_info = LexicalInformation()
        self._token_list: list[Token] = []
        self._error_list: list[str] = []

    @property
    def errors(self) -> list[str]:
        return list(self._error_list)

    def state_error(self, character: str):
        error = 'Unexpected %s on %d:%d, state=%s' % (
            character, self._state_info.line, self._state_info.column, self._state
        )
        self._error_list.append(error)
        self._state = LexicalStates.NIL

    def _is_lexeme_at_end(self, character: str, previous_character: str) -> bool:
        is_whitespace = character.isspace() or _is_line_break(character, previous_character)
        return is_whitespace or character in (self.__terminals.delimiters + self.__terminals.operators)

    def _save_token(self, token_type: TokenTypes):
        new_token = self._state_info.gen_token(token_type)
        if new_token.get_lexeme() != "":
            self._token_list.append(new_token)
        self._state = LexicalStates.NIL

    def _save_full_token(self, lexeme: str, token_type: TokenTypes):
        line, column = self._state_info.line, self._state_info.column
        self._save_token(token_type)
        self._state_info.write_char(lexeme)
        self._state_info.line, self._state_info.column = line, column
        self._save_token(TokenTypes.DELIMITER)

    def _string_state(self, character: str, previous_character: str):
        if character == '"':
            self._save_token(TokenTypes.STRING)
            return
        elif _is_line_break(character, previous_character):
            self.state_error(character)
            return
        self._state_info.write_char(character)

    def _operator_state(self, character: str, previous_character: str):
        char_sum = previous_character + character
        if char_sum.strip() not in self.__terminals.operators:
            self._discover_state(character, previous_character)
            return
        if char_sum in self.__terminals.operators:
            self._state_info.write_char(character)
            self._save_token(TokenTypes.OPERATOR)
        elif previous_character in self.__terminals.operators:
            self._save_token(TokenTypes.OPERATOR)

    def _identifier_state(self, character: str, previous_character: str):
        if self._is_lexeme_at_end(character, previous_character):
            token_type = TokenTypes.IDENTIFIER
            if self.__terminals.is_reserved(self._state_info.lexeme_builder):
                token_type = TokenTypes.RESERVED
            self._save_full_token(character, token_type)
            return
        if (self._state_info.lexeme_builder == "" and character.isnumeric()) or not _is_valid_symbol(character):
            self.state_error(character)
            return

        self._state_info.write_char(character)

    def __number_state(self, character: str, previous_character: str):
        if self._is_lexeme_at_end(character, previous_character) and not (character == "."):
            self._save_full_token(character, TokenTypes.NUMBER)
            return
        if character == ".":
            if self.__state_memory or not previous_character.isnumeric():
                self.state_error(character)
                return
            self.__state_memory = True
        elif previous_character == ".":
            if not character.isnumeric():
                self.state_error(character)
                return
        if self._state_info.lexeme_builder == "":
            self._state_info.write_char(previous_character)
        self._state_info.write_char(character)

    def _comment_state(self, character: str, previous_character: str):
        if self._state == LexicalStates.LINE_COMMENT:
            if _is_line_break(character, previous_character):
                self._save_token(TokenTypes.COMMENT)
                return
        elif previous_character + character == self.__terminals.comments.get(CommentType.BLOCK)[1]:
            self._save_token(TokenTypes.COMMENT)
            return
        self._state_info.write_char(character)

    def _delegate_state(self, character: str, previous_character: str):
        match self._state:
            case LexicalStates.STRING:
                return self._string_state(character, previous_character)
            case LexicalStates.OPERATOR:
                return self._operator_state(character, previous_character)
            case LexicalStates.IDENTIFIER:
                return self._identifier_state(character, previous_character)
            case LexicalStates.NUMBER:
                return self.__number_state(character, previous_character)
            case LexicalStates.LINE_COMMENT | LexicalStates.BLOCK_COMMENT:
                return self._comment_state(character, previous_character)
            case LexicalStates.NIL:
                return

    def _discover_state(self, character: str, previous_character: str) -> None:
        char_sum = previous_character + character
        self._state_info.write_char(character)
        if char_sum == self.__terminals.comments.get(CommentType.LINE)[0]:
            self._state = LexicalStates.LINE_COMMENT
        elif char_sum == self.__terminals.comments.get(CommentType.BLOCK)[0]:
            self._state = LexicalStates.BLOCK_COMMENT
        elif character == '"':
            self._state = LexicalStates.STRING
        elif character.isnumeric():
            self._state = LexicalStates.NUMBER
        elif character.isalpha():
            self._state = LexicalStates.IDENTIFIER

        # Check if it is one of the double operators
        elif char_sum in self.__terminals.operators or character in self.__terminals.operators:
            self._state = LexicalStates.OPERATOR
        elif character in self.__terminals.delimiters:
            self._save_token(TokenTypes.DELIMITER)

    def __process_character(self, character: str, previous_character: str):
        if self._state == LexicalStates.NIL:
            self._discover_state(character, previous_character)
        else:
            self._delegate_state(character, previous_character)

    def __main_loop(self, character: str, previous_character: str):
        self._state_info.column += 1
        # Start processing the character
        self.__process_character(character=character, previous_character=previous_character)
        if _is_line_break(character, previous_character):
            self._state_info.line += 1
            self._state_info.column = 0

    def start(self, char_list: tuple[str]) -> tuple[Token]:
        previous_character = ""

        for character in char_list:
            self.__main_loop(character, previous_character)
            previous_character = character

        if self._state_info.has_ongoing_token():
            self.__process_character("\n", previous_character)
        return tuple(self._token_list)
