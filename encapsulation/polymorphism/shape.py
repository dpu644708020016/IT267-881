import re
from tkinter import N


class Shape:
    def __init__(self)-> None:
        self.__shape = None
        self.__area = 0

    @property #getter
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, value):
        self.__shape = value

    @property #getter
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    #abtrect method
    def compute_area(self):
        pass
