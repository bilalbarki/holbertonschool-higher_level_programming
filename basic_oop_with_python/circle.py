#!/usr/bin/python
from math import pi

''' Class Circle '''
class Circle():
    def __init__(self, radius):
        self.__radius=radius
        self.__center=[0,0]
        self.__color=""
        self.name=""

    def set_center(self, center):
        self.__center=center

    def set_color(self, color):
        self.__color=color

    def get_center(self):
        return self.__center

    def get_color(self):
        return self.__color

    def area(self):
        return pi*self.__radius*self.__radius

    def intersection(self, c_bis):
        '''sum of radii'''
        rad=self.__radius+c_bis.__radius

        '''center distance x-axis'''
        x_axis_d=c_bis.get_center()[0]-self.get_center()[0]

        '''center distance y-axis'''
        y_axis_d=c_bis.get_center()[1]-self.get_center()[1]

        '''r1+r2 <= sqrt((x2-x1)2+(y2-y1)2) they intersect'''
        if (rad**2 > x_axis_d**2 + y_axis_d**2):
            return 1
        else:
            return 0

