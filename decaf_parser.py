# get tokens from lexer
from decaf_lexer import tokens

# define grammar rules

# starting rule????
# def p_program(p):
#     '''
#     program : class_decl*
#     '''

def p_program(p):
    '''
    program : ID
            | ID program
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")