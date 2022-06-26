from empit import EmpIT

#คนที่1
mike = EmpIT('001','Mike',60000)
mike.add_skill('python,Javascript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()
#คนที่2
from empmkt import EmpMKT
anna = EmpMKT('002','Anna',35000)
anna.add_location('Bangkok')
anna.add_commission(30)
anna.emp_detail()
anna.mkt_salary()
#คนที่3
from empmkt import EmpMKT
Jas = EmpMKT('003','Jas',45000)
Jas.add_location('Chiang')
Jas.add_commission(35)
Jas.emp_detail()
Jas.mkt_salary()