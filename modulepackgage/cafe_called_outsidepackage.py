# #วิธีที่ 1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks

#วิธีที่ 2
# from cafe_module import Desserts, Drinks

desserts = Desserts()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drink('สมูตตี้')
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())