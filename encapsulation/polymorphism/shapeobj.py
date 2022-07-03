from secrets import choice
from shapetype import *
#from shapetype import Square Circle Triangle
print("===========คำนวนพื้นที่รูปร่างต่างๆ ===========")
print("1:สี่เหลี่ยม")
print("2:วงกลม")
print("3:สามเหลี่ยม")
choice = int(input("พืั้นที่ที่ต้องการคำนวณ 1-3 :"))
print("================================")

if choice == 1:
    s= Square()
    s.length = float(input("Enter Length: "))
    s.compute_area()
    s.print_square()
elif choice == 2:
    c= Circle()
    c.radius = float(input("Enter radius: "))
    c.compute_area()
    c.print_Circle()
elif choice == 3:
    t= Triangle()
    t.base = float(input("Enter base: "))
    t.high = float(input("Enter high: "))
    t.compute_area()
    t.print_Triangle()
else:
    print("====คุณกรอกผิด_กรุณากรอกใหม่====")