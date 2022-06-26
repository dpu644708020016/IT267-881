class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.area = 0

    def compute(self):\
        self.area = self.width * self.length

    def print_area(self):
        print(f'Rectangle area = {self.area}')

    # def get_data(self):
    #     self.width =float (input("กรุณากรอกความกว้าง :")):
    #     self.length =float (input("กรุณากรอกความยาว :")):

if __name__ == "__main__":
    rac = Rectangle(2,5)
    rac.compute()
    rac.print_area()
    