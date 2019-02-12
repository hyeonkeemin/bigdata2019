class restaurant:
    def __init__(self, name, type, total):
        self.restaurant_name = name
        self.restaurant_type = type
        self.today_customer = 0
        self.today_count = open('./고객서빙현황로그.txt', 'w', encoding='UTF-8')
        self.total_accum = total

    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s 이고 %s 전문점입니다.'%(self.restaurant_name, self.restaurant_type))
        open_message = input('레스토랑을 오픈 하시겠습니까?(y/n) : ')
        if open_message == 'y':
            print('저희 %s 레스토랑이 오픈하였습니다.'%self.restaurant_name)
            self.increment_number_served()
        elif open_message == 'n':print('고생하셨습니다.');return

    def open_restaurant(self):
        print('저희 %s 레스토랑 오픈 했습니다. 어서오세요.'%self.restaurant_name)

    def increment_number_served(self):
        number_served = 0
        while True:
            base_message = str(input('\n어서오세요, 몇명이십니까?(초기화:0 입력, 종료:-1, 누적고객 확인:p)) : '))
            if base_message != 'p':
                if base_message == '0':
                    number_served = 0
                    print('손님카운팅을 0으로 초기화 하였습니다.')
                elif base_message == '-1':
                    print('%s 레스토랑 문닫습니다.'%self.restaurant_name)
                    break
                else:
                    print('%d명 들어오셨습니다. 자리 안내해드리겠습니다.'%int(base_message))
                    number_served += int(base_message)
                    self.today_customer += int(base_message)
            elif base_message == 'p':
                print('지금까지 %d명 오셨습니다.'%number_served)

    def __del__(self):
        self.today_count.write(str(self.today_customer + self.total_accum))
        self.today_count.close()


name_type = input('레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분) : ').split()
today_count_read = open('./고객서빙현황로그.txt', 'r', encoding='UTF-8')
total_accum = int(today_count_read.readline())
a = restaurant(name_type[0], name_type[1], total_accum)
a.describe_restaurant()


# today_count_read = open('./고객서빙현황로그.txt', 'r', encoding='UTF-8')
# total_accum = int(today_count_read.readline())

