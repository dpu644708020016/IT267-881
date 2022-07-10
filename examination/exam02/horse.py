class Horse:
    def __init__(self,max_height:float,name:str,color:str) -> None:
        self.color = color
        self.name = name
        self.max_height = 200

    def run(self,name):
        print(f'{self.name:} is running')

    def show_name(self,name):
        self.name = name

    def show_info(self):
        print(f'*****mule info*****')
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"max_height: {self.max_height} cm")


