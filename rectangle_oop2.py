class Rectangle:
    def __init__(self):
        self.width = 0
        self.length = 0
        self.area = 0
        
    def get_data(self):
        self.width =float (input("Enter width :"))
        self.length =float (input("Enter length :"))

    def compute(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f'Rectangle area = {self.area}')

if __name__ == "__main__":
    rac = Rectangle()
    rac.get_data()
    rac.compute()
    rac.print_area()
    