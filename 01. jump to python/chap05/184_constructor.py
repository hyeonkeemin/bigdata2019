class service:
    secret = '영구는 배꼽이 두 개다'
    name = "" # 가독성을 위해 추가. 좋은습관 ~
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        result = a+b
        print('%s님 %s + %s =  %s 입니다.'%(self.name,a,b,result))

pey = service() # pey는 service의 인스턴스
pey.sum(1, 1) # 이름이 설정되어 있지 않았기 때문에 sum 함수 출력이 완벽하게 되지 않음

