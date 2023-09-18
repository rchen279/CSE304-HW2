# ----------------------------------------------------------------
# Scanner for decaf
#
#
# -------------------------------------------------------------------

# reserved keywords
reserved = {
    "boolean" : "BOOLEAN",
    "break" : "BREAK",
    "continue" : "CONTINUE",
    "class" : "CLASS",
    "do" : "DO",
    "else" : "ELSE",
    "extends" : "EXTENDS",
    "false" : "FALSE",
    "float" : "FLOAT",
    "for" : "FOR",
    "if" : "IF",
    "int" : "INT",
    "new" : "NEW",
    "null" : "NULL",
    "private" : "PRIVATE",
    "public" : "PUBLIC",
    "return" : "RETURN",
    "static" : "STATIC",
    "super" : "SUPER",
    "this" : "THIS",
    "true" : "TRUE",
    "void" : "VOID",
    "while" : "WHILE"
}


# token tuple
tokens = ["IDENTIFIER", # name
          "INTEGER_CONSTANT", #constants
          "FLOAT_CONSTANT",
          "STRING_CONSTANT",
          # syntax stuff and operators
          "LEFT_CURLY_BRACE", # {
          "RIGHT_CURLY_BRACE", # }
          "LEFT_PARENTHESIS", # (
          "RIGHT_PARENTHESIS", # )
          "ASSIGNMENT_OPERATOR", # =
          "POST_INCREMENT_OPERATOR", # X++
          "POST_DECREMENT_OPERATOR", # X--
          "PLUS", # + for addition, unary plus
          "MINUS", # - for subtraction, unary minus
          "TIMES", # * for multiplication
          "DIVIDE", # / for division
          "EQUALITY_OPERATOR", # == equality check
          "DISEQUALITY_OPERATOR", # != inequality
          "LESS_THAN_OPERATOR", # < less than
          "GREATER_THAN_OPERATOR", # > greater than
          "GREATER_THAN_EQUAL_TO_OPERATOR", # >=
          "LESS_THAN_EQUAL_TO_OPERATOR", # <=
          "NEGATION_OPERATOR", # ! negation
          "LOGICAL_AND_OPERATOR", # && AND
          "LOGICAL_OR_OPERATOR", # || operator
          ]

tokens = tokens + list(reserved.values())

# token specifications

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "IDENTIFIER") # check for reserved keywords
    return t

# build the lexer for testing purposes (delete later please)

import ply.lex as lex
# lexer = lex.lex()

# lexer.input("test.txt")
# next_token = lexer.token()
# while next_token != None:
#     print(next_token)
#     next_token = lexer.token()