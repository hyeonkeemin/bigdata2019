class restaurant:

    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print('저희 레스토랑 명칭은 %s 이고 %s 전문점입니다.'%(self.restaurant_name, self.restaurant_type))

    def open_restaurant(self):
        print('저희 %s 레스토랑 오픈 했습니다. 어서오세요.\n'%self.restaurant_name)

    def __del__(self):
        print('%s 레스토랑 문닫습니다.'%self.restaurant_name)

restaurant_list = []
for index_number in range(0, 3):
    restaurant_list.append(input('레스토랑 이름과 요리 재료를 선택하세요(공백으로 구분) : ').split())
    restaurant_list[index_number] = restaurant(restaurant_list[0], restaurant_list[1])
    restaurant_list[index_number].describe_restaurant()
    restaurant_list[index_number].open_restaurant()
#
# for index in range(0, 3):
#     restaurant_list.append(input('입력 : ').split())
#     restaurant_list.restaurant = restaurant(restaurant_list[index][0], restaurant_list[index][1])
#     restaurant_list.restaurant.describe_restaurant()
#     restaurant_list.restaurant.open_restaurant()
print('밤 10시가 되었습니다.')