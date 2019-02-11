class myrestaurant:
    def __init__(self):
        print('저희 레스토랑 오픈햇습니다.')

    def __del__(self): # 클래스가 끝날 때 메모리에서 사라짐 -> 소멸자
        print('레스토랑 문닫습니다.')

korean_restaurant = myrestaurant()
input()