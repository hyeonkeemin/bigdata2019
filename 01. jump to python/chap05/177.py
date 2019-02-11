class service:
    secret = '영구는 배꼽이 두 개다'
    name = "" # 가독성을 위해 추가. 좋은습관 ~
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        result = a+b
        print('%s님 %s + %s =  %s 입니다.'%(self.name,a,b,result))

pey = service() # pey는 service의 인스턴스

print(pey.secret)
pey.setname('홍길동')
pey.sum(1, 2) # pey.sum을 통하여 pey가 호출한지 알기 때문에 pey는 생략 가능
