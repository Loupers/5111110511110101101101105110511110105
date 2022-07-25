#!/usr/bin/python3
import sys

def arabToRom(number):
    z = ""
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            z += sym[i]
            div -= 1
        i -= 1
    return z

def romToArab(rom):
    m = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}
    return m[rom]

def code(s):
    code = ""
    ret = ""
    for x in s:
        if x != ' ':
            num = ord(x) - 96 
            print(num, x)
            code += arabToRom(ord(x) - 96)
            code += ' '
        else:
            code += ' '

    for x in code:
        if x != ' ':
            ret += romToArab(x)
        else:
            ret += ' '

    print(code)
    print(ret)
    return ret

            



for x in sys.argv[1:]:
    print(code(x))

