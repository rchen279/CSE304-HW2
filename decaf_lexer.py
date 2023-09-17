# ----------------------------------------------------------------
# Scanner for decaf
#
#
# -------------------------------------------------------------------

# token tuple
tokens = ("IDENTIFIER", # name
          "INTEGER_CONSTANT", #constants
          "FLOAT_CONSTANT",
          "STRING_CONSTANT",
          # insert keywords ->>>>> what to do ??? 

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
          )

# build the lexer
