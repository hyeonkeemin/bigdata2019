
class restaurant:

    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s 이고 %s 전문점입니다.'%(self.restaurant_name, self.restaurant_type))
        open_message = input('레스토랑을 오픈 하시겠습니까?(y/n) : ')
        if open_message == 'y':
            print('저희 %s 레스토랑이 오픈하였습니다.'%self.restaurant_name)
            self.number_served()
        elif open_message == 'n':print('고생하셨습니다.');return

    def open_restaurant(self):
        print('저희 %s 레스토랑 오픈 했습니다. 어서오세요.'%self.restaurant_name)

    def number_served(self):
        base_number = 0
        while True:
            base_message = str(input('\n어서오세요, 몇명이십니까?(초기화:0 입력, 종료:-1, 누적고객 확인:p)) :'))
            add_number = int(base_message) + base_number
            if base_message == '0':
                add_number = 0
                print('손님카운팅을 0으로 초기화 하였습니다.')
            elif base_message == '-1':
                print('%s 레스토랑 문닫습니다.'%self.restaurant_name)
                break
            else:
                print('%d명 들어오셨습니다. 자리 안내해드리겠습니다.'%add_number)


name_type = input('레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분) : ').split()
a = restaurant(name_type[0], name_type[1])
a.describe_restaurant()

