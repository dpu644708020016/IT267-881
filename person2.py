class Person:
    def __init__(self,name:str,sex:str,profession:str,study:int):
        self.name = name
        self.sex = sex
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name:} working as a {self.profession}')

    def show(self):
        print(f'Name:{self.name } Sex: {self.sex} Profession: {self.profession} Study: {self.study}')

    def __del__(self):
        print("object was destroyed")

if __name__ == '__main__':
    #person1
    Jassa = Person('Jassa','Female','Softwere Enhiner',0)
    Jassa.work()
    Jassa.show()
    #person2
    Jon = Person('Jon','male','Doctor',15)
    Jon.work()
    Jon.show()
    #person3
    Lisa = Person('Lisa','Female','Singer',10)
    Lisa.work()
    Lisa.show()


