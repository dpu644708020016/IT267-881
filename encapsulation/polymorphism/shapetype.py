from shape import Shape
from math import pi
#abstect class การกำหนดโครงสร้าง
class Square(Shape):
    def __init__(self,length = 0)-> None:
        super().__init__()
        self.Square = ("Shape")
        self.__length = length

    @property #getter
    def length(self):
        return self.__length

    @length.setter
    def length(self,value):
        self.__length = value

    def compute_area(self):
        super().compute_area()
        self.area = self.length ** 2

    def print_square(self):
        print(f'{self.shape} area ={self.area:,.2f}')

class Circle(Shape):
    def __init__(self,radius = 0)-> None:
        super().__init__()
        self.shape = "Circle"
        self.__radius = radius

    @property #getter
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def compute_area(self):
        super().compute_area()
        self.area = pi *(self.radius ** 2)

    def print_Circle(self):
        print(f'{self.shape} Area ={self.area:,.2f}')


class Triangle(Shape):
    def __init__(self,base = 0,high = 0)-> None:
        super().__init__()
        self.shape = "Triangle"
        self.__base = base
        self.__high = high

    @property #getter base
    def base(self):
        return self.__base

    @base.setter #setter base
    def base(self, value):
        self.__base = value

    @property #getter base
    def high(self):
        return self.__high

    @high.setter #setter base
    def high(self, value):
        self.__high = value

    def compute_area(self):
        super().compute_area()
        self.area = 0.5 * self.base * self.high

    def print_Triangle(self):
        print(f'{self.shape} Area ={self.area:,.2f}')