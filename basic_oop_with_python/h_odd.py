#!/usr/bin/python
'''Returns one if an odd number is encountered, otherwise 1'''
def odd(x):
    if (type(x) != int):
        return 0
    if (x % 2 == 1):
        return 1
    else:
        return 0
