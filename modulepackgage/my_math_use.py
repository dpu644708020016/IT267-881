#วิธีที่ 1
from my_math import sqrt,circle_area

print(f'sqrt of 5 ={sqrt(5)}')
print(f'circle area = {circle_area(2):,.2f}')

#วิธีที่ 2
import my_math as my #ถ้าใส่ชื่อเล่นต้องใส่ทุกฟังชั่น
print("****วิธีที่ 2****")
print(f'sqrt of 5 = {my.sqrt(5)}')
print(f'circle area = {my.circle_area(2):,.2f}')