class Person:
    def __init__(self,name,sex,profession):
        self.name = name
        self.sex = sex
        self.profession = profession
        self.study = 0 #สร้างตัวแปรเพิ่มใส่ 0

    def work(self):
        print(f'{self.name:} working as a {self.profession}') #ต้องการปริ้นชื่อตามชื่ออาชีพ ใส่fคือการเอาตัวแปรใส่เข้าไปใน str

    def study(self):
        self.study = hours

    def show(self):
        print(f'Name:{self.name } Sex: {self.sex} Profession: {self.profession} Study: {self.study}')

#person1
Jassa = Person('Jassa','Female','Softwere Enhineer')
Jassa.work()
Jassa.study=10
Jassa.show()
#person2
Jon = Person('Jon','male','Doctor')
Jon.work()
Jon.study=15
Jon.show()
#person3
Lisa = Person('Lisa','Female','Singer')
Lisa.work()
Lisa.study=10
Lisa.show()
