#!/usr/bin/env python

# Compiler usage: csc input.cs

import sys
import lexer
import syntax
import logging

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " <input.cs>")
    exit(1)

# Define a filename.
filename = sys.argv[1]

print("Compiling " + filename + "...")

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.read()

lex = lexer.lexer_input(content)

syntax.syntax_input(lex, content)
