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
    '''statement : asignment SEMICOLON'''
    p[0] = p[1]

def p_asignment(p):
    '''asignment : TYPE IDENTIFIER ASSIGNMENT INTEGER_LITERAL'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def syntax_input(lexer, content, log):
    parser = yacc.yacc()
    return parser.parse(content)

