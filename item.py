class Item:
    def __init__(self,name:str,price:float,quantity = 1)-> None:
#ตรวจสอบ price, guantity ว่าต้องมากกว่า > 0
        assert price > 0,f"Price {price} most greater than 0"
        assert quantity > 0,f"Quantity {quantity} most greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    #Instance method ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ method นี้ได้ต้องสร้าง object
    def total_price(self):
        return self.price * self.quantity
    #self.total_price = total_price * self.quantity
    #return self.total

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    item1 = Item("Monitor",5600)
    item2 = Item("Mouse",1500,2)
    print("=== Total Price ===")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")