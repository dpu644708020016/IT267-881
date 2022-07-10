class JuiceOrder:
    def __init__(self,menu:str,size:"R",price:int,num=1)->None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.num = num
        self.price = 0

    def check_menu(self):
        menu_Dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
        }
    def compute_price(self):
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)
        if self.size == 'R':
            self.price += 1
        elif self.size == 'L':
            self.price += 5
        else:
            self.price

        JuiceOrder.total = self.price * self.num

    def display(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu}({self.size}{self.num} * {self.price} => {JuiceOrder.total}baht'

    def __del__(self):
        print("Object was destroyed")

    if __name__ == "__main__":
        order1 = JuiceOrder('WJ','L')
        order2 = JuiceOrder('OJ','R')
        order1 = JuiceOrder('PJ','L')

    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())

