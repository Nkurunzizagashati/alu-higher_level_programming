#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        l = i - 32
    else:
        l = i
    print('{}'.format(chr(l)), end='')
