# get tokens from lexer
from decaf_lexer import tokens

# define grammar rules
# starting rule -- program
def p_program(p):
    '''
    program : class_decl program
            | empty
    '''

# empty production
def p_empty(p):
    'empty :'
    pass

def p_class_declaration(p):
    '''
    class_decl : CLASS id optionalExtendsId L_CURLY_BRACE class_body_decl_plus R_CURLY_BRACE
    '''

def p_optionalExtendsId(p):
    '''
    optionalExtendsId : EXTENDS id
                | empty
    '''

def p_classBodyDeclPlus(p):
    '''
    class_body_decl_plus : class_body_decl
                        | class_body_decl class_body_decl_plus
    '''

def p_class_body_decl(p):
    '''
    class_body_decl : field decl
                    | method_decl
                    | constructor_decl
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")