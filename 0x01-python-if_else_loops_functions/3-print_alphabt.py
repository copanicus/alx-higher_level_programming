#!/usr/bin/python3

for x in range(ord('a'), ord('z') + 1):
    if chr(x) != 'q' and chr(x) != 'e':
        print('{:c}'.format(chr(x)), end='')
