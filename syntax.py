#!/usr/bin/env python

import ply.yacc as yacc
import ply.lex as lex
import lexer

tokens = lexer.tokens

def p_start(p):
    'start : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_statement(p):
    '''statement : asignment
                 | CONST asignment
                 | block_statement
                 | call SEMICOLON'''
    p[0] = p[1]

def p_asignment(p):
    '''asignment : type IDENTIFIER ASSIGNMENT expression SEMICOLON'''
    p[0] = p[1]

def p_expression(p):
    '''expression : int_expression
                  | double_expression
                  | string_expression
                  | bool_expression
                  | call'''

def p_block_statement(p):
    '''block_statement : if
                       | while'''

def p_if(p):
    '''if : IF LPAREN bool_expression RPAREN block_or_statement else'''

def p_else(p):
    '''else : ELSE block_or_statement
            | empty'''

def p_while(p):
    '''while : WHILE LPAREN bool_expression RPAREN block_or_statement'''

def p_block_or_statement(p):
    '''block_or_statement : statement
                          | block'''

def p_block(p):
    '''block : LBRACKET statement_list RBRACKET'''

def p_int_expression(p):
    '''int_expression : INTEGER_LITERAL'''
    p[0] = p[1]

def p_fqn(p):
    '''fqn : IDENTIFIER
           | fqn DOT IDENTIFIER'''

def p_type_name(p):
    '''type_name : type IDENTIFIER''' 

def p_arguments(p):
    '''arguments : arguments COMMA type_name
                | type_name
                | empty'''

def p_arguments_call(p):
    '''arguments_call : arguments_call COMMA expression
                      | expression
                      | empty'''

def p_call(p):
    '''call : fqn LPAREN arguments_call RPAREN'''

def p_double_expression(p):
    '''double_expression : DOUBLE_LITERAL'''
    p[0] = p[1]

def p_string_expression(p):
    '''string_expression : STRING_LITERAL'''
    p[0] = p[1]

def p_bool_expression(p):
    '''bool_expression : TRUE
                       | FALSE'''
    p[0] = p[1]

def p_type(p):
    '''type : INT
            | DOUBLE
            | STRING
            | BOOL'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error on line " + str(p.lineno))
    print("Unexpected : " + str(p.value))

def syntax_input(lexer, content):
    parser = yacc.yacc()
    return parser.parse(content)

