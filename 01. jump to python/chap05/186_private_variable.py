class service:
    secret = '영구는 배꼽이 두 개다' # 클래스가 가지는 고유의 공통 속성
    name = "" # 가독성을 위해 추가. 좋은습관 ~
    def __init__(self, name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        print('%s님 %s + %s =  %s 입니다.'%(self.name,a,b,result))

pey = service('홍길동') # 객체만이 가지는 고유의 초기값을 설정하고 싶을 때 생성자를 활용한다.

print(pey.secret) # 정말로 보호되어야 하는 변수라면 이렇게 제공하면 안됨


