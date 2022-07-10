from horse import Horse
from donkey import Donkey
class Mule(Horse,Donkey):
    def __init__(self,max_height:float,name:str,color:str) -> None:
        Donkey.__init__(self, max_height, name, color)
        Horse.__init__(self,age,weight)

    def run(self,name):
        print(f'{self.name:} is running')

    def show_info(self):
        print(f'*****mule info*****')
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"max_height: {self.max_height} cm")
        print(f"Age: {self.age}")
        print(f"weight: {self.weight} kg")
