#เรียกใช้ package เพื่อเข้าใช้คลาส Customer, Account
from bank.customer import Customer
from bank.account import Account
#สร้าง objeat ของ customer
paul = Customer()
paul.new_customer()

paul_acc = Account()
paul_acc.open_account(paul.name,'saving','0123-4578',500)

print('==== Customer Detail ====')
print(paul.cus_info())
print(paul_acc.display_balance())