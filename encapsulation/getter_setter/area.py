class Area:
    def __init__(self)-> None:
        self.base = 0
        self.high = 0

    @property #getter ของ dase
    def base(self):
        return self.__base
    #setter ของ dase
    @base.setter
    def base(self, value):
        self.__base = value

    @property#getter ของ high
    def high(self):
        return self.__high
    #setter ของ high
    @high.setter
    def high(self, value):
        self.__high = value

    def compute_area(self):
        return (0.5*self.base* self.high)
    #return 0.5* self.__base * self.__high