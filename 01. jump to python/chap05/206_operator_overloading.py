class housepark: # 부모 클래스(super class)
    __last_name__ = "박"
    full_name = ''
    def __init__(self, name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print('%s, %s 여행을 가다.'%(self.full_name, where))
    def love(self, who):
        print('%s, %s 사랑에 빠졌네'%(self.full_name, who.full_name))
    def __add__(self, who):
        print('%s, %s 결혼했네'%(self.full_name, who.full_name))

class housekim(housepark): # 자식 클래스(child class)
    __last_name__ = '김'
    def travel(self, where, day):
        print('%s, %s 여행 %d일 가다'%(self.full_name, where, day))

pey=housepark('응용')
juliet=housekim('줄리엣')
pey.travel('대구')
juliet.travel('대구', 3)
pey.love(juliet)
pey+juliet