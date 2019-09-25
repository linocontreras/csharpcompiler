#!/usr/bin/env python

import ply.lex as lex

keywords = (
    
)
# List of token names.   This is always required
tokens = (
'IDENTIFIER',
# Operators
'OPERATOR',
# Assignments
'ASSIGNMENT',
# Literals
'INTEGER_LITERAL',
'REAL_LITERAL',
'BOOLEAN_LITERAL',
'STRING_LITERAL',
# Delimiters
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
)

# Regular expression rules for simple tokens
t_IDENTIFIER = r'([a-zA-Z]|_)(_|[a-zA-Z]|[0-9])*'
t_OPERATOR    = r'\+|-|\*|/'
t_ASSIGNMENT = r'=|\+=|-=|\*|/'
t_INTEGER_LITERAL = r'[0-9]+'
t_REAL_LITERAL = r'[0-9]+.[0-9]+((e|E)(\+|-)?[0-9]+)?'
t_BOOLEAN_LITERAL = r'true|false'
t_STRING_LITERAL = r'"(.*)"'

# Delimiters
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENT(t):
    r'//.*'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
def tokens(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(str(lexer.lineno) + ': ' + str(tok))
        


