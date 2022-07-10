class Area:
    def __init__(self,base=0,high=0)-> None:
        self.__base = base
        self.__high = high

    @property #getter ของ base
    def base(self):
        return self.__base
    #setter ของ base
    @base.setter
    def base(self, value):
        self.__base = value
    @base.deleter
    def base(self):
        print('Deleting base')
        del self.__base
    @property#getter ของ high
    def high(self):
        return self.__high
    #setter ของ high
    @high.setter
    def high(self, value):
        self.__high = value
    @high.deleter
    def high(self):
        print('Deleting high')
        del self.__high

    def compute_area(self):
        return (0.5*self.base* self.high)
    #return 0.5* self.__base * self.__high