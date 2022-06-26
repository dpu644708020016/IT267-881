from employee import Employee

class EmpIT(Employee): #EmpTI ได้ตัวแปรจาก Employee ทั้งหมดแล้ว
    def __init__(self,id, name, salary)-> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.department = 'IT'

    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,experience:str):
        self.experience = experience

    def add_emp_detail(self):
        super().emp_detail()
        print (f'skill: {self.skill}')
        print(f'experience: {self.experience}')

    def it_salary(self):
        self._emp_salary()