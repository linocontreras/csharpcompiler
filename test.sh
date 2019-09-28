#!/usr/bin/bash

for filename in tests/*.cs; do
    [ -e "$filename" ] || continue
    ./csc.py "$filename"
done