class restaurant:

    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s 이고 %s 전문점입니다.'%(self.restaurant_name, self.restaurant_type))

    def open_restaurant(self):
        print('저희 %s 레스토랑 오픈 했습니다. 어서오세요.\n'%self.restaurant_name)

    def __del__(self):
        if b == 3:
            print('저녁 10시가 되었습니다.')
            print('%s 레스토랑 문닫습니다.'%self.restaurant_name)

b = 0
d = ['']
while b < 3:
    for i in d:
        name_type = input('레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분) : ').split()
        a = restaurant(name_type[0], name_type[1])
        a.describe_restaurant()
        a.open_restaurant()
        b += 1





