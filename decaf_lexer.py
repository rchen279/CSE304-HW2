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


# token tuple -> to modify
tokens = ["ID", # identifier
          "INT_CONST", #constants
          "FLOAT_CONST",
          "STRING_CONST",
          # syntax stuff and operators
          "L_CURLY_BRACE", # {
          "R_CURLY_BRACE", # }
          "L_PAREN", # (
          "R_PAREN", # )
          "SEMI_COLON", # ;
          "ASSIGNMENT_OP", # =
          "POST_INCR_OP", # X++
          "POST_DECR_OP", # X--
          "PLUS", # + for addition, unary plus
          "MINUS", # - for subtraction, unary minus
          "TIMES", # * for multiplication
          "DIVIDE", # / for division
          "EQUALITY_OP", # == equality check
          "DISEQUALITY_OP", # != inequality
          "L_THAN_OP", # < less than
          "G_THAN_OP", # > greater than
          "G_THAN_EQUAL_TO_OP", # >=
          "L_THAN_EQUAL_TO_OP", # <=
          "NEG_OP", # ! negation
          "LOGICAL_AND_OP", # && AND
          "LOGICAL_OR_OP", # || operator
          ]

tokens = tokens + list(reserved.values())

# token specifications

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "ID") # check for reserved keywords
    return t

# build the lexer for testing purposes (delete later please)

import ply.lex as lex
# lexer = lex.lex()

# lexer.input("test.txt")
# next_token = lexer.token()
# while next_token != None:
#     print(next_token)
#     next_token = lexer.token()