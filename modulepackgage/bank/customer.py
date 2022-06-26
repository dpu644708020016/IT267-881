class Customer:
    def __init__(self)-> None:
        self.name = ''
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input(f'Enter Name :')
        self.address = input(f'Enter Address :')
        self.phone = input(f'Enter Phone :')

    def cus_info(self):
        info = f'Name:{self.name}\naddress:{self.address}\nphone:{self.phone}'
        return info