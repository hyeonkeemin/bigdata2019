class housepark: # 부모 클래스(super class)
    __last_name__ = "박"
    full_name = ''
    def __init__(self, name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print('%s, %s 여행을 가다.'%(self.full_name, where))

class housekim(housepark): # 자식 클래스(child class)
    __last_name__ = '김'
    def travel(self, where, day):
        print('%s, %s 여행 %d일 가다'%(self.full_name, where, day))

kitty=housekim("만복")
kitty.travel('제주', 23) # method overriding