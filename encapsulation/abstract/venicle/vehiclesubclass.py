from re import T
from this import s
from vehicleabsteact import vehicle
class Car(vehicle):
    def __init__(self,band,speed)->None:
        super().__init__(band,speed)
        self.__year = 0
        self.__maintanance = 0

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value

    @property
    def maintanance (self):
        return self.__maintanance
    @maintanance.setter
    def maintanance(self,value):
        self.__maintanance = value

    def show_detail(self):
        super().show_detail()
        print("====== Car details ======")
        print(f'{self.band} with speed {self.speed} km/hr')
        print(f'maintanance in {self.maintanance}')

class Truck (vehicle):
    def __init__(self,band,speed)->None:
        super().__init__(band,speed)
        self.__capacity = 1000
        self.__wheel = 4

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self,value):
        self.__capacity = value

    @property
    def wheel(self):
        return self.__wheel
    @wheel.setter
    def wheel(self,value):
        self.__wheel = value

    def show_detail(self):
        super().show_detail()
        print("====== Truck details ======")
        print(f'{self.band} with speed {self.speed} km/hr and {self.wheel}')
        print(f'capacity in {self.capacity} tons.')
    def show_detail(self):
        print(++++ Truck price ++++)
        if self.wheel == 4:
            price = 1000
        elif self.wheel == 6:
            price = 1500
        elif self.wheel == 8:
            price = 2000
        else:
            price = 3000
        print(f'{self.wheel} wheels truck is {price} Baht/Day.')


class Motorcycle (vehicle):
    def __init__(self,band,speed)->None:
        super().__init__(band,speed)
        self.__cc = 150
        self.__model = ""

    @property
    def cc(self):
        return self.__cc
    @cc.setter
    def cc(self,cc):
        self.__cc = cc

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model = model

    def show_detail(self):
        super().show_detail()
        print("====== Motorcycle details ======")
        print(f'{self.band} -- {self.model} with speed {self.speed}km/hr has {self.cc} cc.')

