class Account:
    def __init__(self)-> None:
        self.acc_type = ''
        self.acc_no = ''
        self.acc_balance = 0

    def open_account(self,acc_name,acc_type,acc_on,acc_balance):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_on = acc_on
        self.acc_balance = acc_balance

    def display_balance(self):
        return f'{self.acc_name} has {self.acc_balance} baht'