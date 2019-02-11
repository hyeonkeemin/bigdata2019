class housepark: # 부모 클래스(super class)
    __last_name__ = "박"
    full_name = ''
    def __init__(self, name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print('%s, %s 여행을 가다.'%(self.full_name, where))

class housekim(housepark): # 자식 클래스(child class)
    __last_name__ = '김'
    pass

kitty=housekim("만복") # __last_name__ 변수를 부모클래스나 자식클래스 똑같이 쓰지만 김씨에 맞게 오버라이딩 됨(에러안남)
kitty.travel('제주')
