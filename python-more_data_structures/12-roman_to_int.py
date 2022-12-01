#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    total = 0
    sum = dict(I=1, X=10, L=50, V=5, C=100, D=500, M=1000)
    for current, next in zip(roman_string, roman_string[1:]):
        if sum[current] >= sum[next]:
            total += sum[current]
        else:
            total -= sum[current]
    total += sum[roman_string[-1]]
    return total
