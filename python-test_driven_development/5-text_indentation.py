#!/usr/bin/python3
# a function that prints a text with 2 new lines after
# each of these characters: ., ? and :
"""
    define function 'text_indentation'
"""


def text_indentation(text):
    """
        this function will print a text with two new lines
        after each of these characters: '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    n = 0
    while n < len(text) and text[n] == ' ':
        n += 1
    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[n] in ".?:":
            if text[n] in ".?:":
                print("\n")
                n += 1
                while n < len(text) and text[n] == ' ':
                    n += 1
                continue
            n += 1
