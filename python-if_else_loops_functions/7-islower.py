#!/usr/bin/python3
def islower(c):
    for i in c:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            return True
        else:
            return False
