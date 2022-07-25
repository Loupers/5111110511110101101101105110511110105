#!/usr/bin/python3
import sys

def code(word):
    count = 0
    for x in word:
        if x != ' ':
            count += ord(x) - 96
    return count % 31

for x in sys.argv[1:]:
    print(code(x))
