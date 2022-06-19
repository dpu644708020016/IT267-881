class Bird:
    global Bird_type #ถ้าไม้ใส่ว่า global ตัวแปร Bird_type จะกลาย เป็น Class variables ทันที
    Bird_type = 'parrot'
    bird_name = 'Lori'#class variables

    def __init__(self,color) -> None:
        self.color = color#instance variables
        name = 'Peter'#local variables
        print (f'{name} in int')

if __name__ == "__main__":
    my_bird = Bird('Green,Blue')
    #call instance variables ชื่อวัตถุ.ชื่อตัวแปร
    print(my_bird.color)

    #call class variables ชื่อคลาส
    print(Bird.bird_name)

    #call global variables เรียกชื่อตัวแปร
    print(Bird_type)

    #error
    #พยายามเรียก local   variables
    #print(name)#Nameerror : name 'name' is not defined
    #พยายามเรียก global  variables ผ่าน Class
    #print(Bird.bird_type)
    #type object 'bird' has no attribute 'bird_type'