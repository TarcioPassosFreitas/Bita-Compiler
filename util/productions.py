class GrammarDefinition:
    def __init__(self):
        self.string_chars = "{Printable} + {HT} - [\"]"
        self.ide = "{Letter}{AlphaNumeric}* | {Letter}"
        self.string = "'\"' {String Chars}* '\"'"
        self.int = "{Number}+"
        self.real = "{Number}+'.'{Number}+"
        self._first_set = {
            "<incr>": {
                "++",
                "--"
            },
            "<mult>": {
                "*",
                "/"
            },
            "<soma>": {
                "+",
                "-"
            },
            "<log_operator>": {
                "!",
                "||",
                "&&"
            },
            "<rel>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!="
            },
            "<boolean>": {
                "true",
                "false"
            },
            "<valor>": {
                "ide",
                "true",
                "false",
                "int",
                "real",
                "string"
            },
            "<tipo>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide"
            },
            "<var>": {
                "var"
            },
            "<variable_access>": {
                "ide"
            },
            "<var_var>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                ""
            },
            "<var_aux2>": {
                "ide"
            },
            "<var_attribution>": {
                "=",
                ""
            },
            "<atrib>": {
                "="
            },
            "<var2>": {
                ",",
                ""
            },
            "<const>": {
                "const",
                ",",
                ";"
            },
            "<var_const>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                ""
            },
            "<const_aux>": {
                "ide"
            },
            "<struct_bloco>": {
                "struct"
            },
            "<struct_var>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                ""
            },
            "<struct_aux>": {
                "ide"
            },
            "<vetor>": {
                "ide"
            },
            "<struct2>": {
                ",",
                ";"
            },
            "<log>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide",
                "true",
                "false"
            },
            "<log2>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<log3>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<exp>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<exp_2>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<exp_3>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<exp_4>": {
                "(",
                "int",
                "real",
                "ide"
            },
            "<struct_exp>": {
                "ide"
            },
            "<log_aux>": {
                "!",
                "||",
                "&&",
                ""
            },
            "<log2_aux>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                ""
            },
            "<log_expression_attrib>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                ""
            },
            "<_log>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide",
                "true",
                "false"
            },
            "<_log2>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<_log3>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<_log_aux>": {
                "!",
                "||",
                "&&",
                ""
            },
            "<_log2_aux>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                ""
            },
            "<exp_aux>": {
                "+",
                "-",
                ""
            },
            "<exp_2_aux>": {
                "*",
                "/",
                ""
            },
            "<exp_3_aux>": {
                "++",
                "--",
                ""
            },
            "<parametro>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide"
            },
            "<multi_param>": {
                ",",
                ""
            },
            "<declararG>": {
                "function",
                "procedure",
                "struct",
                ""
            },
            "<if>": {
                "if"
            },
            "<while>": {
                "while"
            },
            "<else>": {
                "else",
                ""
            },
            "<codigo>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                ""
            },
            "<print>": {
                "print"
            },
            "<read>": {
                "read"
            },
            "<var_manipulation>": {
                "=",
                ".",
                "(",
                "["
            },
            "<code_attribution>": {
                "=",
                ".",
                "("
            },
            "<struct>": {
                "."
            },
            "<function>": {
                "("
            },
            "<functionline>": {
                "("
            },
            "<array>": {
                "["
            },
            "<vector_access>": {
                "["
            },
            "<vector_position>": {
                "ide",
                "int"
            },
            "<matrix_access>": {
                "[",
                ""
            },
            "<element_access>": {
                "[",
                ""
            },
            "<blocoR>": {
                "ide"
            },
            "<valorPrint2>": {
                "(",
                "string",
                "++",
                "--",
                "int",
                "real",
                "ide",
                "true",
                "false",
                ""
            },
            "<valorPrintAux>": {
                "(",
                "string",
                "++",
                "--",
                "int",
                "real",
                "ide",
                "true",
                "false",
                ",",
                ""
            },
            "<valorPrint>": {
                ",",
                ""
            },
            "<bloco>": {
                "(",
                "string",
                "++",
                "--",
                "int",
                "real",
                "ide",
                "true",
                "false",
                ",",
                ""
            },
            "<start>": {
                "function",
                "procedure",
                "struct",
                "var",
                "const",
                ",",
                ";",
                "start"
            },
            "<final>": {
                "start"
            },
            "<start1>": {
                "function",
                "procedure",
                "struct",
                "var",
                "start"
            },
            "<start2>": {
                "function",
                "procedure",
                "struct",
                "const",
                ",",
                ";",
                "start"
            },
            "<start final>": {
                "function",
                "procedure",
                "struct",
                "start"
            }
        }
        self._follow_set = {
            "<start>": {
                "$"
            },
            "<incr>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ","
            },
            "<exp_3_aux>": {
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "++",
                "--"
            },
            "<exp_3>": {
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "++",
                "--"
            },
            "<exp_2>": {
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "*",
                "/"
            },
            "<exp>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "+",
                "-"
            },
            "<log3>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ","
            },
            "<log2>": {
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!="
            },
            "<log>": {
                "!",
                "||",
                "&&",
                ")",
                ";",
                ","
            },
            "<log_aux>": {
                "!",
                "||",
                "&&"
            },
            "<valorPrint2>": {
                ",",
                ")"
            },
            "<valorPrintAux>": {
                ")"
            },
            "<valorPrint>": {
                ")"
            },
            "<bloco>": {
                ")"
            },
            "<log2_aux>": {
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!="
            },
            "<log_expression_attrib>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ","
            },
            "<exp_aux>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "+",
                "-"
            },
            "<exp_2_aux>": {
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "*",
                "/"
            },
            "<mult>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<soma>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<log_operator>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide",
                "true",
                "false"
            },
            "<rel>": {
                "++",
                "--",
                "(",
                "int",
                "real",
                "ide"
            },
            "<boolean>": {
                "const",
                ",",
                ";",
                "!",
                "||",
                "&&",
                ")"
            },
            "<valor>": {
                "const",
                ",",
                ";"
            },
            "<_log>": {
                "!",
                "||",
                "&&",
                ")"
            },
            "<_log_aux>": {
                "!",
                "||",
                "&&"
            },
            "<tipo>": {
                "ide"
            },
            "<var>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}",
                "function",
                "procedure",
                "struct",
                "const",
                ",",
                ";",
                "start"
            },
            "<codigo>": {
                "return",
                "}"
            },
            "<var_manipulation>": {
                "return",
                "}"
            },
            "<variable_access>": {
                ",",
                "=",
                "}",
                ";"
            },
            "<var_aux2>": {
                "=",
                "}",
                ";"
            },
            "<var_var>": {
                "}"
            },
            "<var2>": {
                "=",
                "}",
                ";"
            },
            "<var_attribution>": {
                ";"
            },
            "<const>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                "}",
                "function",
                "procedure",
                "struct",
                "var",
                "start"
            },
            "<const_aux>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                "}"
            },
            "<var_const>": {
                "}"
            },
            "<struct_bloco>": {
                "function",
                "procedure",
                "struct",
                "var",
                "const",
                ",",
                ";",
                "start"
            },
            "<declararG>": {
                "function",
                "procedure",
                "struct",
                "var",
                "const",
                ",",
                ";",
                "start"
            },
            "<struct_var>": {
                "}"
            },
            "<struct_aux>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                "}"
            },
            "<struct2>": {
                "int",
                "real",
                "boolean",
                "string",
                "ide",
                "}"
            },
            "<_log2>": {
                "!",
                "||",
                "&&",
                ")",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!="
            },
            "<_log2_aux>": {
                "!",
                "||",
                "&&",
                ")",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!="
            },
            "<_log3>": {
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")"
            },
            "<exp_4>": {
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ","
            },
            "<parametro>": {
                ")"
            },
            "<multi_param>": {

            },
            "<if>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<while>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<else>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<code_attribution>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<vector_position>": {
                "]"
            },
            "<vector_access>": {
                ",",
                "=",
                "}",
                ";",
                ")",
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                "["
            },
            "<matrix_access>": {
                ",",
                "=",
                "}",
                ";",
                ")",
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&"
            },
            "<array>": {
                "=",
                ",",
                ";",
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")"
            },
            "<vetor>": {
                ",",
                ";",
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")"
            },
            "<element_access>": {
                ")"
            },
            "<blocoR>": {
                ")"
            },
            "<function>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}",
                ",",
                ")"
            },
            "<functionline>": {
                "++",
                "--",
                "*",
                "/",
                "+",
                "-",
                ">",
                "<",
                ">=",
                "<=",
                "==",
                "!=",
                "!",
                "||",
                "&&",
                ")",
                ";",
                ",",
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<atrib>": {
                ",",
                ";",
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<struct>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<struct_exp>": {
                "("
            },
            "<read>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<print>": {
                "if",
                "while",
                "print",
                "read",
                "var",
                "ide",
                "return",
                "}"
            },
            "<start1>": {
                "$"
            },
            "<start2>": {
                "$"
            },
            "<start final>": {
                "$"
            },
            "<final>": {
                "$"
            }
        }
        self.productions = {
            "<incr>": [
                ['++'],
                ['--']
            ],
            "<mult>": [
                ['*'],
                ['/']
            ],
            "<soma>": [
                ['+'],
                ['-']
            ],
            "<log_operator>": [
                ['!'],
                ['||'],
                ['&&']
            ],
            "<rel>": [
                ['>'],
                ['<'],
                ['>='],
                ['<='],
                ['=='],
                ['!=']
            ],
            "<boolean>": [
                ['true'],
                ['false']
            ],
            "<valor>": [
                ['ide'],
                ['<boolean>'],
                ['int'],
                ['real'],
                ['string']
            ],
            "<tipo>": [
                ['int'],
                ['real'],
                ['boolean'],
                ['string'],
                ['ide']
            ],
            "<var>": [
                ['var', '{', '<var_var>', '}']
            ],
            "<variable_access>": [
                ['ide', '<matrix_access>']
            ],
            "<var_var>": [
                ['<tipo>', '<var_aux2>', '<var_attribution>', ';', '<var_var>'],
                ['']
            ],
            "<var_aux2>": [
                ['<variable_access>', '<var2>']
            ],
            "<var_attribution>": [
                ['<atrib>', '<var2>'],
                ['']
            ],
            "<var2>": [
                [',', '<var_aux2>'],
                ['']
            ],
            "<const>": [
                ['const', '{', '<var_const>', '}'],
                [',', '<const_aux>'],
                [';']
            ],
            "<var_const>": [
                ['<tipo>', '<const_aux>', '<var_const>'],
                ['']
            ],
            "<const_aux>": [
                ['ide', '=', '<valor>', '<const>']
            ],
            "<struct_bloco>": [
                ['struct', 'ide', '{', '<struct_var>', '}']
            ],
            "<struct_var>": [
                ['<tipo>', '<struct_aux>', '<struct_var>'],
                ['ide', '<struct_aux>', '<struct_var>'],
                ['']
            ],
            "<struct_aux>": [
                ['ide', '<struct2>'],
                ['<vetor>', '<struct2>']
            ],
            "<struct2>": [
                [',', '<struct_aux>'],
                [';']
            ],
            "<log>": [
                ['<log2>', '<log_aux>'],
                ['<boolean>', '<log_aux>']
            ],
            "<log_aux>": [
                ['<log_operator>', '<log>', '<log_aux>'],
                ['']
            ],
            "<log2>": [
                ['<log3>', '<log2_aux>']
            ],
            "<log2_aux>": [
                ['<rel>', '<log2>', '<log2_aux>'],
                ['']
            ],
            "<log3>": [
                ['<exp>', '<log_expression_attrib>'],
                ['(', '<log>', ')']
            ],
            "<log_expression_attrib>": [
                ['<rel>', '<exp>'],
                ['']
            ],
            "<_log>": [
                ['<_log2>', '<_log_aux>'],
                ['<boolean>', '<_log_aux>']
            ],
            "<_log_aux>": [
                ['<log_operator>', '<_log>', '<_log_aux>'],
                ['']
            ],
            "<_log2>": [
                ['<_log3>', '<_log2_aux>']
            ],
            "<_log2_aux>": [
                ['<rel>', '<_log2>', '<_log2_aux>'],
                ['']
            ],
            "<_log3>": [
                ['<exp>', '<rel>', '<exp>'],
                ['(', '<_log>', ')']
            ],
            "<exp>": [
                ['<exp_2>', '<exp_aux>']
            ],
            "<exp_aux>": [
                ['<soma>', '<exp>', '<exp_aux>'],
                ['']
            ],
            "<exp_2>": [
                ['<exp_3>', '<exp_2_aux>']
            ],
            "<exp_2_aux>": [
                ['<mult>', '<exp_2>', '<exp_2_aux>'],
                ['']
            ],
            "<exp_3>": [
                ['<incr>', '<exp_3>', '<exp_3_aux>'],
                ['<exp_4>', '<exp_3_aux>']
            ],
            "<exp_3_aux>": [
                ['<incr>', '<exp_3_aux>'],
                ['']
            ],
            "<exp_4>": [
                ['(', '<exp>', ')'],
                ['int'],
                ['real'],
                ['ide'],
                ['<vetor>'],
                ['<struct_exp>', '<functionline>']
            ],
            "<parametro>": [
                ['<tipo>', 'ide', '<matrix_access>', '<multi_param>']
            ],
            "<multi_param>": [
                [',', '<parametro>'],
                ['']
            ],
            "<declararG>": [
                ['function', '<tipo>', 'ide', '(', '<parametro>', ')', '{', '<codigo>', 'return', '<log>', ';', '}'],
                ['procedure', 'ide', '(', '<parametro>', ')', '{', '<codigo>', '}'],
                ['<struct_bloco>'],
                ['']
            ],
            "<if>": [
                ['if', '(', '<_log>', ')', 'then', '{', '<codigo>', '}', '<else>']
            ],
            "<while>": [
                ['while', '(', '<_log>', ')', '{', '<codigo>', '}']
            ],
            "<else>": [
                ['else', '{', '<codigo>', '}'],
                ['']
            ],
            "<codigo>": [
                ['<if>', '<codigo>'],
                ['<while>', '<codigo>'],
                ['<print>', '<codigo>'],
                ['<read>', '<codigo>'],
                ['<var>', '<codigo>'],
                ['ide', '<var_manipulation>'],
                ['']
            ],
            "<var_manipulation>": [
                ['<code_attribution>', '<codigo>'],
                ['<array>', '<atrib>', '<codigo>']
            ],
            "<code_attribution>": [
                ['<atrib>'],
                ['<struct>'],
                ['<function>'],
                ['<functionline>']
            ],
            "<vector_position>": [
                ['ide'],
                ['int']
            ],
            "<vector_access>": [
                ['[', '<vector_position>', ']']
            ],
            "<matrix_access>": [
                ['<vector_access>'],
                ['']
            ],
            "<array>": [
                ['<vector_access>', '<matrix_access>']
            ],
            "<vetor>": [
                ['ide', '<array>']
            ],
            "<function>": [
                ['(', '<bloco>', ')']
            ],
            "<functionline>": [
                ['(', '<bloco>', ')', ';']
            ],
            "<atrib>": [
                ['=', '<log>', ';']
            ],
            "<struct>": [
                ['.', 'ide', '=', '<log>', ';']
            ],
            "<struct_exp>": [
                ['ide', '.', 'ide']
            ],
            "<read>": [
                ['read', '(', '<blocoR>', ')', ';']
            ],
            "<element_access>": [
                ['<array>'],
                ['']
            ],
            "<blocoR>": [
                ['ide', '<element_access>']
            ],
            "<print>": [
                ['print', '(', '<valorPrintAux>', ')', ';']
            ],
            "<valorPrint2>": [
                ['<function>'],
                ['string'],
                ['<log>'],
                ['']
            ],
            "<valorPrintAux>": [
                ['<valorPrint2>', '<valorPrint>']
            ],
            "<valorPrint>": [
                [',', '<valorPrintAux>'],
                ['']
            ],
            "<bloco>": [
                ['<valorPrintAux>']
            ],
            "<start>": [
                ['<declararG>', '<start>'],
                ['<var>', '<start2>'],
                ['<const>', '<start1>'],
                ['<final>']
            ],
            "<start1>": [
                ['<declararG>', '<start1>'],
                ['<var>', '<start final>'],
                ['<final>']
            ],
            "<start2>": [
                ['<declararG>', '<start2>'],
                ['<const>', '<start final>'],
                ['<final>']
            ],
            "<start final>": [
                ['<declararG>', '<start final>'],
                ['<final>']
            ],
            "<final>": [
                ['start', '{', '<codigo>', '}']
            ]
        }

    def first(self, production_name: str) -> set[str]:
        result = self._first_set[production_name]
        if result is None:
            result = {}
        return result

    def follow(self, production_name: str) -> set[str]:
        result = self._follow_set[production_name]
        if result is None:
            result = {}
        return result
