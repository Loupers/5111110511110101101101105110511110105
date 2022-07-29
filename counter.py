#!/usr/bin/env python3
import sys

for x in sys.argv[1:]:
	print(sum(ord(c) - 64 for c in x.upper().replace(' ', '')) % 31)
