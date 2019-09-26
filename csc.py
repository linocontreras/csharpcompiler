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

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

lex = lexer.lexer_input(content, log)

syntax.syntax_input(lex, content, log)
