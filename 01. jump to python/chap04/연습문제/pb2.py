ingredient_list=[]

def input_ingredient():

    while True:
        input_ingredient_message=str(input('원하시는 재료를 선택하세요(모두 선택 시 \'종료\' 입력) : '))
        if input_ingredient_message == '종료':
            break
        else:
            print('%s 주문받았습니다.'%input_ingredient_message)
            ingredient_list.append(input_ingredient_message)
            print('추가 한 재료 : ', ingredient_list)

    return

def make_sandwiches():
    print('샌드위치를 만들겠습니다.')

    for sandwiches_message in ingredient_list:
        print('%s 추가합니다.'%sandwiches_message)

    return


while True:
    first_message = str(input('''안녕하세요, 저희 가게에 방문해 주셔서 감사합니다.
     1. 주문
     2. 종료
     입력 : '''))

    if (first_message == '1. 주문') or (first_message=='주문') or (first_message == '1'):
        input_ingredient()
        make_sandwiches()
        print('여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.')
        break

    elif (first_message == '2. 종료') or (first_message == '종료') or (first_message == '2'):
        print('방문해 주셔서 감사합니다.')
        break