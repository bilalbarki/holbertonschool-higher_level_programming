#!/usr/bin/python
import math

'''Number class'''
class Number(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, sum):
        self.__value = sum

    '''operators'''
    def __add__(self,x):
        return Number(self.__value + x.__value)

    def __sub__(self,x):
        return Number(self.__value - x.__value)

    def __mul__(self,x):
        return Number(self.__value * x.__value)

    def __div__(self,x):
        return Number(self.__value / x.__value)

    def __str__(self):
        return str(self.__value)
