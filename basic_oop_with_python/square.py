#!/usr/bin/python

''' Class Square '''
class Square():
    def __init__(self, side_length):
        self.__side_length=side_length
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
        return self.__side_length*self.__side_length

    def __str__(self):
        sq=""
        for i in range(0,self.__side_length):
            sq+="*"
        sq+="\n"
        for i in range(0,self.__side_length-2):
            sq+="*"
            for k in range(0,self.__side_length-2):
                sq+=" "
            sq+="*\n"
        for i in range(0,self.__side_length):
            sq+="*"
        return sq
