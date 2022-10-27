#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            f = chr(ord(i) - 32)
        else:
            f = i
        print('{:s}'.format(f), end='')
    print('')
