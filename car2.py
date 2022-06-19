from calendar import c
from re import T


class Car:
    brand = "TOYOTA"

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def printCarDetail(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}")
#staticmethod ไม่มีค่าว่า self
    @staticmethod
    def get_static_method():
        text = "Static"
        print(f"In {text} method")
    #
    #
#Class methodsm ต้องมี cls เสมอ
    @classmethod
    def get_class_method(cls):
        my_text = "class"
        print(f"This is {my_text} method")

    def __del__(self):
        print("Object was destroyed")

if __name__ == '__main__':
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail()

#้เรียกใช้ Static method
    Car.get_static_method() #เรียกใช้ผ่าน class
    my_car.get_static_method() #เรียกใช้ผ่าน instance/object

#้เรียกใช้ Class method
    Car.get_class_method() #เรียกใช้ผ่าน class
    my_car.get_class_method() #เรียกใช้ผ่าน instance/object