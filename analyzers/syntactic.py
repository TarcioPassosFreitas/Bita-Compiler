from typing import Callable

from models.business.sythatic_node import SynthaticNode
from models.errors.synthatic_errors import SynthaticParseErrors
from util.data_structure.queue import Queue
from util.productions import GrammarDefinition
from util.token_types import TokenTypes

productions_functions: dict[GrammarDefinition, Callable[[Queue, list[SynthaticParseErrors]], SynthaticNode]]


def sp_incr(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<incr>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '++':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '--':
        node.add(token_queue.remove())

    return node


def sp_mult(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    """
    This function parse tokens for production <mult>\n
    Accepted productions below\n
    [17:14 `'*'` <terminal>]\n
    [18:7 `'/'` <terminal>]\n
    """

    node = SynthaticNode(production='<mult>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '*':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '/':
        node.add(token_queue.remove())

    return node


def sp_soma(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<soma>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '+':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '-':
        node.add(token_queue.remove())

    return node


def sp_log_operator(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log_operator>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '!':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '||':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '&&':
        node.add(token_queue.remove())

    return node


def sp_rel(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<rel>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '>':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '<':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '>=':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '<=':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '==':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '!=':
        node.add(token_queue.remove())

    return node


def sp_boolean(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<boolean>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'true':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == 'false':
        node.add(token_queue.remove())

    return node


def sp_valor(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<valor>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<boolean>'):
        temp = sp_boolean(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.NUMBER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.NUMBER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.STRING:
        node.add(token_queue.remove())

    return node


def sp_tipo(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<tipo>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'int':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == 'real':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == 'boolean':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() == 'string':
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())

    return node


def sp_var(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'var':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<var>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_var>') or token_verification:
            temp = sp_var_var(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<var>', ['}'], token_queue.peek()))

    return node


def sp_variable_access(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<variable_access>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<matrix_access>'):
            temp = sp_matrix_access(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_var_var(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var_var>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<tipo>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_tipo(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_aux2>') or token_verification:
            temp = sp_var_aux2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<var_var>', list(GrammarDefinition().first('<var_aux2>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var_attribution>'):
            temp = sp_var_attribution(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<var_var>', [';'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_var>') or token_verification:
            temp = sp_var_var(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_var_aux2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var_aux2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<variable_access>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_variable_access(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var2>'):
            temp = sp_var2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_var_attribution(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var_attribution>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<atrib>'):
        temp = sp_atrib(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var2>'):
            temp = sp_var2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_var2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == ',':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_aux2>') or token_verification:
            temp = sp_var_aux2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<var2>', list(GrammarDefinition().first('<var_aux2>')), token_queue.peek()))

    else:
        return node

    return node


def sp_const(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<const>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'const':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<const>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_const>') or token_verification:
            temp = sp_var_const(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<const>', ['}'], token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() == ',':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<const_aux>') or token_verification:
            temp = sp_const_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<const>', list(GrammarDefinition().first('<const_aux>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() == ';':
        node.add(token_queue.remove())

    return node


def sp_var_const(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var_const>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<tipo>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_tipo(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<const_aux>') or token_verification:
            temp = sp_const_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<var_const>', list(GrammarDefinition().first('<const_aux>')), token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<var_const>') or token_verification:
            temp = sp_var_const(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_const_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<const_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '=':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<const_aux>', ['='], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.STRING
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<valor>') or token_verification:
            temp = sp_valor(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<const_aux>', list(GrammarDefinition().first('<valor>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<const>'):
            temp = sp_const(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<const_aux>', list(GrammarDefinition().first('<const>')), token_queue.peek()))

    return node


def sp_struct_bloco(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct_bloco>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'struct':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct_bloco>', ['ide'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct_bloco>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_var>') or token_verification:
            temp = sp_struct_var(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct_bloco>', ['}'], token_queue.peek()))

    return node


def sp_struct_var(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct_var>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<tipo>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_tipo(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_aux>') or token_verification:
            temp = sp_struct_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<struct_var>', list(GrammarDefinition().first('<struct_aux>')),
                                                   token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_var>') or token_verification:
            temp = sp_struct_var(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_aux>') or token_verification:
            temp = sp_struct_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<struct_var>', list(GrammarDefinition().first('<struct_aux>')),
                                                   token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_var>') or token_verification:
            temp = sp_struct_var(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_struct_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<struct2>'):
            temp = sp_struct2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<struct_aux>', list(GrammarDefinition().first('<struct2>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<vetor>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_vetor(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<struct2>'):
            temp = sp_struct2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<struct_aux>', list(GrammarDefinition().first('<struct2>')), token_queue.peek()))

    return node


def sp_struct2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == ',':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<struct_aux>') or token_verification:
            temp = sp_struct_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<struct2>', list(GrammarDefinition().first('<struct_aux>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() == ';':
        node.add(token_queue.remove())

    return node


def sp_log(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<log2>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_log2(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log_aux>'):
            temp = sp_log_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<boolean>'):
        temp = sp_boolean(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log_aux>'):
            temp = sp_log_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_log_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log_operator>'):
        temp = sp_log_operator(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log>') or token_verification:
            temp = sp_log(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<log_aux>', list(GrammarDefinition().first('<log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log_aux>'):
            temp = sp_log_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_log2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<log3>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_log3(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log2_aux>'):
            temp = sp_log2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_log2_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log2_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<rel>'):
        temp = sp_rel(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log2>') or token_verification:
            temp = sp_log2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<log2_aux>', list(GrammarDefinition().first('<log2>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log2_aux>'):
            temp = sp_log2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_log3(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log3>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<exp>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_exp(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log_expression_attrib>'):
            temp = sp_log_expression_attrib(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '(':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log>') or token_verification:
            temp = sp_log(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<log3>', list(GrammarDefinition().first('<log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<log3>', [')'], token_queue.peek()))

    return node


def sp_log_expression_attrib(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<log_expression_attrib>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<rel>'):
        temp = sp_rel(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp>') or token_verification:
            temp = sp_exp(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<log_expression_attrib>', list(GrammarDefinition().first('<exp>')),
                                                   token_queue.peek()))

    else:
        return node

    return node


def sp_l_og(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<_log>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<_log2>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_l_og2(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<_log_aux>'):
            temp = sp_l_og_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<boolean>'):
        temp = sp_boolean(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<_log_aux>'):
            temp = sp_l_og_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_l_og_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<_log_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<log_operator>'):
        temp = sp_log_operator(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<_log>') or token_verification:
            temp = sp_l_og(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<_log_aux>', list(GrammarDefinition().first('<_log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<_log_aux>'):
            temp = sp_l_og_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_l_og2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<_log2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<_log3>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_l_og3(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<_log2_aux>'):
            temp = sp_l_og2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_l_og2_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<_log2_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<rel>'):
        temp = sp_rel(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<_log2>') or token_verification:
            temp = sp_l_og2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<_log2_aux>', list(GrammarDefinition().first('<_log2>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<_log2_aux>'):
            temp = sp_l_og2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_l_og3(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<_log3>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<exp>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_exp(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<rel>'):
            temp = sp_rel(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<_log3>', list(GrammarDefinition().first('<rel>')), token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp>') or token_verification:
            temp = sp_exp(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<_log3>', list(GrammarDefinition().first('<exp>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() == '(':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<_log>') or token_verification:
            temp = sp_l_og(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<_log3>', list(GrammarDefinition().first('<_log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<_log3>', [')'], token_queue.peek()))

    return node


def sp_exp(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<exp_2>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_exp_2(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_aux>'):
            temp = sp_exp_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_exp_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<soma>'):
        temp = sp_soma(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp>') or token_verification:
            temp = sp_exp(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<exp_aux>', list(GrammarDefinition().first('<exp>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_aux>'):
            temp = sp_exp_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_exp_2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<exp_3>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_exp_3(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_2_aux>'):
            temp = sp_exp_2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_exp_2_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_2_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<mult>'):
        temp = sp_mult(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp_2>') or token_verification:
            temp = sp_exp_2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<exp_2_aux>', list(GrammarDefinition().first('<exp_2>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_2_aux>'):
            temp = sp_exp_2_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_exp_3(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_3>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<incr>'):
        temp = sp_incr(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp_3>') or token_verification:
            temp = sp_exp_3(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<exp_3>', list(GrammarDefinition().first('<exp_3>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_3_aux>'):
            temp = sp_exp_3_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<exp_4>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_exp_4(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_3_aux>'):
            temp = sp_exp_3_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_exp_3_aux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_3_aux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<incr>'):
        temp = sp_incr(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<exp_3_aux>'):
            temp = sp_exp_3_aux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_exp_4(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<exp_4>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<exp>') or token_verification:
            temp = sp_exp(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<exp_4>', list(GrammarDefinition().first('<exp>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<exp_4>', [')'], token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.NUMBER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.NUMBER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<vetor>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_vetor(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<struct_exp>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_struct_exp(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<functionline>'):
            temp = sp_functionline(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<exp_4>', list(GrammarDefinition().first('<functionline>')), token_queue.peek()))

    return node


def sp_parametro(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<parametro>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<tipo>') or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_tipo(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<parametro>', ['ide'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<matrix_access>'):
            temp = sp_matrix_access(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<multi_param>'):
            temp = sp_multi_param(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_multi_param(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<multi_param>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == ',':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<parametro>') or token_verification:
            temp = sp_parametro(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<multi_param>', list(GrammarDefinition().first('<parametro>')),
                                                   token_queue.peek()))

    else:
        return node

    return node


def sp_declararg(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<declararG>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'function':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<tipo>') or token_verification:
            temp = sp_tipo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<declararG>', list(GrammarDefinition().first('<tipo>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['ide'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<parametro>') or token_verification:
            temp = sp_parametro(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<declararG>', list(GrammarDefinition().first('<parametro>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == 'return':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['return'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log>') or token_verification:
            temp = sp_log(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<declararG>', list(GrammarDefinition().first('<log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', [';'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['}'], token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() == 'procedure':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['ide'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<parametro>') or token_verification:
            temp = sp_parametro(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<declararG>', list(GrammarDefinition().first('<parametro>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<declararG>', ['}'], token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<struct_bloco>'):
        temp = sp_struct_bloco(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    else:
        return node

    return node


def sp_if(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<if>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'if':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<if>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<_log>') or token_verification:
            temp = sp_l_og(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<if>', list(GrammarDefinition().first('<_log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<if>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == 'then':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<if>', ['then'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<if>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<if>', ['}'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<else>'):
            temp = sp_else(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_while(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<while>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'while':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<while>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<_log>') or token_verification:
            temp = sp_l_og(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<while>', list(GrammarDefinition().first('<_log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<while>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<while>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<while>', ['}'], token_queue.peek()))

    return node


def sp_else(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<else>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'else':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<else>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<else>', ['}'], token_queue.peek()))

    else:
        return node

    return node


def sp_codigo(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<codigo>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<if>'):
        temp = sp_if(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<while>'):
        temp = sp_while(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<print>'):
        temp = sp_print(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<read>'):
        temp = sp_read(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var>'):
        temp = sp_var(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var_manipulation>'):
            temp = sp_var_manipulation(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<codigo>', list(GrammarDefinition().first('<var_manipulation>')),
                                                   token_queue.peek()))

    else:
        return node

    return node


def sp_var_manipulation(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<var_manipulation>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<code_attribution>'):
        temp = sp_code_attribution(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<array>'):
        temp = sp_array(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<atrib>'):
            temp = sp_atrib(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<var_manipulation>', list(GrammarDefinition().first('<atrib>')),
                                                   token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_code_attribution(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<code_attribution>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<atrib>'):
        temp = sp_atrib(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<struct>'):
        temp = sp_struct(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<function>'):
        temp = sp_function(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<functionline>'):
        temp = sp_functionline(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_vector_position(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<vector_position>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.NUMBER:
        node.add(token_queue.remove())

    return node


def sp_vector_access(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<vector_access>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '[':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER or temp_token_type == TokenTypes.NUMBER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<vector_position>') or token_verification:
            temp = sp_vector_position(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<vector_access>', list(GrammarDefinition().first('<vector_position>')),
                                     token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ']':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<vector_access>', [']'], token_queue.peek()))

    return node


def sp_matrix_access(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<matrix_access>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<vector_access>'):
        temp = sp_vector_access(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    else:
        return node

    return node


def sp_array(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<array>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<vector_access>'):
        temp = sp_vector_access(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<matrix_access>'):
            temp = sp_matrix_access(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_vetor(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<vetor>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<array>'):
            temp = sp_array(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<vetor>', list(GrammarDefinition().first('<array>')), token_queue.peek()))

    return node


def sp_function(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<function>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<bloco>') or token_verification:
            temp = sp_bloco(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<function>', [')'], token_queue.peek()))

    return node


def sp_functionline(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<functionline>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<bloco>') or token_verification:
            temp = sp_bloco(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<functionline>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<functionline>', [';'], token_queue.peek()))

    return node


def sp_atrib(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<atrib>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '=':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log>') or token_verification:
            temp = sp_log(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<atrib>', list(GrammarDefinition().first('<log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<atrib>', [';'], token_queue.peek()))

    return node


def sp_struct(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == '.':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct>', ['ide'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == '=':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct>', ['='], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<log>') or token_verification:
            temp = sp_log(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<struct>', list(GrammarDefinition().first('<log>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct>', [';'], token_queue.peek()))

    return node


def sp_struct_exp(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<struct_exp>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '.':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct_exp>', ['.'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<struct_exp>', ['ide'], token_queue.peek()))

    return node


def sp_read(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<read>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'read':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<read>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<blocoR>') or token_verification:
            temp = sp_blocor(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<read>', list(GrammarDefinition().first('<blocoR>')), token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<read>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<read>', [';'], token_queue.peek()))

    return node


def sp_element_access(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<element_access>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<array>'):
        temp = sp_array(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    else:
        return node

    return node


def sp_blocor(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<blocoR>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.IDENTIFIER:
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<element_access>'):
            temp = sp_element_access(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    return node


def sp_print(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<print>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'print':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '(':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<print>', ['('], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<valorPrintAux>') or token_verification:
            temp = sp_valorprintaux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == ')':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<print>', [')'], token_queue.peek()))
        if token_queue.peek() and token_queue.peek().get_lexeme() == ';':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<print>', [';'], token_queue.peek()))

    return node


def sp_valorprint2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<valorPrint2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<function>'):
        temp = sp_function(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    elif token_queue.peek() and token_queue.peek().get_token_type() == TokenTypes.STRING:
        node.add(token_queue.remove())

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<log>') or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_log(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    else:
        return node

    return node


def sp_valorprintaux(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<valorPrintAux>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<valorPrint2>') or temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_valorprint2(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<valorPrint>'):
        temp = sp_valorprint(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_valorprint(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<valorPrint>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == ',':
        node.add(token_queue.remove())
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<valorPrintAux>') or token_verification:
            temp = sp_valorprintaux(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)

    else:
        return node

    return node


def sp_bloco(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<bloco>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
            '<valorPrintAux>') or temp_token_type == TokenTypes.STRING or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.NUMBER or temp_token_type == TokenTypes.IDENTIFIER:
        temp = sp_valorprintaux(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_start(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<start>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<declararG>'):
        temp = sp_declararg(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start>'):
            temp = sp_start(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
            else:
                error_list.append(
                    SynthaticParseErrors('<start>', list(GrammarDefinition().first('<start>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var>'):
        temp = sp_var(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start2>'):
            temp = sp_start2(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start>', list(GrammarDefinition().first('<start2>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<const>'):
        temp = sp_const(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start1>'):
            temp = sp_start1(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start>', list(GrammarDefinition().first('<start1>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<final>'):
        temp = sp_final(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_start1(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<start1>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<declararG>'):
        temp = sp_declararg(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start1>'):
        temp = sp_start1(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start1>', list(GrammarDefinition().first('<start1>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<var>'):
        temp = sp_var(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start final>'):
            temp = sp_start_final(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start1>', list(GrammarDefinition().first('<start final>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<final>'):
        temp = sp_final(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_start2(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<start2>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<declararG>'):
        temp = sp_declararg(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start2>'):
        temp = sp_start2(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start2>', list(GrammarDefinition().first('<start2>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<const>'):
        temp = sp_const(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start final>'):
            temp = sp_start_final(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        else:
            error_list.append(
                SynthaticParseErrors('<start2>', list(GrammarDefinition().first('<start final>')), token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<final>'):
        temp = sp_final(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_start_final(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<start final>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<declararG>'):
        temp = sp_declararg(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
    if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<start final>'):
        temp = sp_start_final(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)
        else:
            error_list.append(SynthaticParseErrors('<start final>', list(GrammarDefinition().first('<start final>')),
                                                   token_queue.peek()))

    elif token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first('<final>'):
        temp = sp_final(token_queue, error_list)
        if temp and temp.is_not_empty():
            node.add(temp)

    return node


def sp_final(token_queue: Queue, error_list: list[SynthaticParseErrors]) -> SynthaticNode:
    node = SynthaticNode(production='<final>')
    if not token_queue.peek():
        return node
    temp_token_type = token_queue.peek().get_token_type()
    if token_queue.peek() and token_queue.peek().get_lexeme() == 'start':
        node.add(token_queue.remove())
        if token_queue.peek() and token_queue.peek().get_lexeme() == '{':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<final>', ['{'], token_queue.peek()))
        temp_token_type = token_queue.peek() and token_queue.peek().get_token_type()
        token_verification = temp_token_type == TokenTypes.IDENTIFIER
        if token_queue.peek() and token_queue.peek().get_lexeme() in GrammarDefinition().first(
                '<codigo>') or token_verification:
            temp = sp_codigo(token_queue, error_list)
            if temp and temp.is_not_empty():
                node.add(temp)
        if token_queue.peek() and token_queue.peek().get_lexeme() == '}':
            node.add(token_queue.remove())
        else:
            error_list.append(SynthaticParseErrors('<final>', ['}'], token_queue.peek()))

    return node
