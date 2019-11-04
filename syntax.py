#!/usr/bin/env python

import ply.yacc as yacc
import ply.lex as lex
import lexer
from node import *

tokens = lexer.tokens

def p_start(p):
    '''start : class_list'''
    p[0] = Node('program', [p[1]])

def p_class_list(p):
    '''class_list : class_list class
                  | empty'''
    if len(p) == 3:
        p[0] = Node('class_list', [p[1], p[2]])
    else:
        p[0] = Node('class_list')

def p_class(p):
    '''class : access CLASS IDENTIFIER LBRACKET class_body RBRACKET'''
    p[0] = Node('class', [p[1], p[5]], p[3])

def p_class_body(p):
    '''class_body : class_body method
                  | class_body class_variable
                  | class_body constant
                  | empty'''
    if len(p) == 3:
        p[0] = Node('class_body', [p[1], p[2]])
    else:
        p[0] = Node('class_body')

# def p_method_list(p):
#     '''method_list : method_list method
#                    | empty'''
#     if len(p) == 3:
#         p[0] = Node('method_list', [p[1], p[2]])
#     else:
#         p[0] = Node('method_list')

def p_class_variable(p):
    '''class_variable : access type IDENTIFIER SEMICOLON
                      | access type IDENTIFIER ASSIGNMENT expression SEMICOLON'''
    if len(p) == 5:
        p[0] = Node('class_variable', [p[1], p[2]], p[3])
    else:
        p[0] = Node('class_variable', [p[1], p[2], p[5]], f'{p[3]} {p[4]}')


def p_method(p):
    '''method : access type IDENTIFIER LPAREN arguments RPAREN block'''
    p[0] = Node('method', [p[1], p[2], p[5], p[7]], p[3])

def p_access(p):
    '''access : PUBLIC
              | PRIVATE
              | empty'''
    if p[1] is not None:
        p[0] = Node('access', None, p[1])
    else:
        p[0] = Node('access')

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = Node('statement_list', [p[1], p[2]])
    else:
        p[0] = Node('statement_list')

def p_statement(p):
    '''statement : var_declaration
                 | asignment
                 | constant
                 | block_statement
                 | call SEMICOLON'''
    p[0] = Node('statement', [p[1]])

def p_constant(p):
    '''constant : CONST var_declaration'''
    p[0] = Node('constant', [p[2]])

def p_var_declaration(p):
    '''var_declaration : type IDENTIFIER SEMICOLON
                       | type IDENTIFIER ASSIGNMENT expression SEMICOLON'''
    if len(p) == 4:
        p[0] = Node('var_declaration', [p[1]], p[2])
    else:
        p[0] = Node('var_declaration', [p[1], p[4]], f'{p[2]} {p[3]}')

def p_asignment(p):
    '''asignment : fqn ASSIGNMENT expression SEMICOLON'''
    p[0] = Node('assignment', [p[1], p[3]], p[2])

def p_expression(p):
    '''expression : int_expression
                  | double_expression
                  | string_expression
                  | bool_expression
                  | call'''
    p[0] = Node('expression', [p[1]])

def p_block_statement(p):
    '''block_statement : if
                       | while'''
    p[0] = Node('block_statement', [p[1]])

def p_if(p):
    '''if : IF LPAREN expression RPAREN block_or_statement else'''
    p[0] = Node('if', [p[3], p[5], p[6]])

def p_else(p):
    '''else : ELSE block_or_statement
            | empty'''
    if len(p) == 3:
        p[0] = Node('else', [p[2]])
    else:
        p[0] = Node('else')

def p_while(p):
    '''while : WHILE LPAREN expression RPAREN block_or_statement'''
    p[0] = Node('while', [p[3], p[5]])

def p_block_or_statement(p):
    '''block_or_statement : statement
                          | block'''
    p[0] = Node('block_or_statement', [p[1]])

def p_block(p):
    '''block : LBRACKET statement_list RBRACKET'''
    p[0] = Node('block', [p[2]])

def p_int_expression(p):
    '''int_expression : INTEGER_LITERAL'''
    p[0] = Node('int_expression', None, p[1])

def p_fqn(p):
    '''fqn : IDENTIFIER
           | fqn DOT IDENTIFIER'''
    if len(p) == 2:
        p[0] = Node('fqn', None, p[1])
    else:
        p[0] = Node('fqn', [p[1]], p[3])

def p_type_name(p):
    '''type_name : type IDENTIFIER'''
    p[0] = Node('type_name', [p[1]], p[2]) 

def p_arguments(p):
    '''arguments : arguments COMMA type_name
                | type_name
                | empty'''
    if len(p) == 4:
        p[0] = Node('arguments', [p[1], p[3]])
    elif p[1] is not None:
        p[0] = Node('arguments', [p[1]])
    else:
        p[0] = Node('arguments')

def p_arguments_call(p):
    '''arguments_call : arguments_call COMMA expression
                      | expression
                      | fqn
                      | empty'''
    if len(p) == 4:
        p[0] = Node('arguments_call', [p[1], p[3]])
    elif len(p) == 1:
        p[0] = Node('arguments_call', [p[1]])
    else:
        p[0] = Node('arguments_call')

def p_call(p):
    '''call : fqn LPAREN arguments_call RPAREN'''
    p[0] = Node('call', [p[3], p[1]])

def p_double_expression(p):
    '''double_expression : DOUBLE_LITERAL'''
    p[0] = Node('double_expression', None, p[1])

def p_string_expression(p):
    '''string_expression : STRING_LITERAL'''
    p[0] = Node('string_expression', None, p[1])

def p_bool_expression(p):
    '''bool_expression : TRUE
                       | FALSE'''
    p[0] = Node('bool_expression', None, p[1])

def p_type(p):
    '''type : INT
            | DOUBLE
            | STRING
            | BOOL
            | VOID'''
    p[0] = Node('type', None, p[1])

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error on line " + str(p.lineno))
    print("Unexpected: " + str(p.value))

def syntax_input(lexer, content):
    lexer.lineno = 1
    parser = yacc.yacc()
    return parser.parse(content)

