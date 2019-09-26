#!/usr/bin/env python

import ply.lex as lex
import re

keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'const': 'CONST'
}
# List of token names.   This is always required
tokens = list(keywords.values()) + [
'IDENTIFIER',
# Operators
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
# Assignments
'ASSIGNMENT',
# Literals
'INTEGER_LITERAL',
'REAL_LITERAL',
'BOOLEAN_LITERAL',
'STRING_LITERAL',
# Types
'TYPE',
# Delimiters
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'SEMICOLON',
]

def t_IDENTIFIER(t):
    r'([a-zA-Z]|_)(_|[a-zA-Z]|[0-9])*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    if t.type == 'IDENTIFIER':
        if re.match(t_TYPE, t.value) != None:
            t.type = 'TYPE'
    return t

# Regular expression rules for simple tokens
t_TYPE = r'int|float|bool|string'

# Operators
t_PLUS    = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_ASSIGNMENT = r'=|\+=|-=|\*=|/='

# Types

# Literals
t_INTEGER_LITERAL = r'[0-9]+'
t_REAL_LITERAL = r'[0-9]+.[0-9]+((e|E)(\+|-)?[0-9]+)?'
t_BOOLEAN_LITERAL = r'true|false'
t_STRING_LITERAL = r'"(.*)"'

# Delimiters
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_SEMICOLON = r';'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENT(t):
    r'(//.*)|(/\*(.|\n)*\*/)'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Give the lexer some input
def lexer_input(data):
    lexer = lex.lex() #lex.lex(debug=True,debuglog=log)
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break
        #print(str(tok))
    return lexer
        


