from this import s
from acc import ABC, abstractmethond

class Vehicle(ABC):
    def __init__(self,brand,speed)-> None:
        super().__init__()
        self.brand = brand
        self.speed = speed
        self.gear = 0
        self.seat = 0

    @bstractmethond
    def show_detail(self):
        pass