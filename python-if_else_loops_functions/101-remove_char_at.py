#!/usr/bin/python3
def remove_char_at(str, n):
    position = 0
    new = ''
    for i in str:
        if position != n:
            new = new + i
        position = position + 1
    return new
