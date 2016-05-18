#!/usr/bin/python
import math

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
        return math.pi*self.__radius*self.__radius

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

    def intersection_percentage(self, c_bis):
        '''intersection percentage'''
        if (self.intersection(c_bis) == 0):
            return 0
        radius = self.__radius
        radius2 = c_bis.__radius
        RADIUS1 = radius ** 2
        RADIUS2 = radius2 ** 2
        XAXIS = c_bis.get_center()[0] - self.get_center()[0]
        YAXIS = c_bis.get_center()[1] - self.get_center()[1]
        XYSQUARE = XAXIS ** 2 + YAXIS ** 2
        distance = math.sqrt(XAXIS ** 2 + YAXIS ** 2)
        if (distance==0 and radius == 0 and radius2 == 0):
            return 100
        elif (radius == 0 and radius2 == 0):
            return 0;
        if (radius > radius2 and distance == 0):
            return RADIUS2/RADIUS1 * 100.0
        elif (distance == 0):
            return 100;
        if (distance + radius2 < radius):
            return RADIUS2 / RADIUS1 * 100.0
        elif (distance + radius < radius2):
            return 100
        
        area = RADIUS1 * math.acos((XYSQUARE + RADIUS1 - RADIUS2)/(2 * distance * radius)) + RADIUS2 * math.acos((XYSQUARE + RADIUS2 - RADIUS1)/(2 * distance * radius2)) - (1./2) * math.sqrt((-distance+radius+radius2)*(distance+radius-radius2)*(distance-radius+radius2)*(distance+radius+radius2))
        return  area / (math.pi * RADIUS1) * 100
