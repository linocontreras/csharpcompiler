#!/usr/bin/env python

# Compiler usage: csc input.cs

import sys
import lexer
import syntax
import logging

argc = len(sys.argv)

if argc < 2 or argc > 3:
    print("Usage: " + sys.argv[0] + " [-ast] <input.cs>")
    exit(1)

if argc == 2:
    filename = sys.argv[1]
    ast = False

if argc == 3:
    if sys.argv[1] != '-ast':
        print("Usage: " + sys.argv[0] + " [-ast] <input.cs>")
        exit(1)
    ast = True
    filename = sys.argv[2]

# Define a filename.

print("Compiling " + filename + " ...")

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.read()

lex = lexer.lexer_input(content)

root = syntax.syntax_input(lex, content)

if ast:
    root.printAST()
