class Student:
    student = "Student"

    def __init__(self,id:str,name:str,major="IT") ->None:
        self.id = id
        self.name = name
        self.major = major

    def DisplayDetail(self):
        print(f"Student: {self.student}")
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    Jessica = Student(111,"Jessica","IT")
    Jessica.DisplayDetail()

    John = Student(222,"John","MKT")
    John.DisplayDetail()

    James = Student(113,"James")
    James.DisplayDetail()