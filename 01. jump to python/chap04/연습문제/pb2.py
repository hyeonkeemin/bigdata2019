ingredient_list=[]
def input_ingredient():
    while True:
        ingredient_select = str(input('안녕하세요, 원하시는 재료를 입력하세요 : '))
        if ingredient_select != '종료' or ingredient_select != '2':
            ingredient_list.append(ingredient_select)
            print('추가한거 : ', ingredient_list)
        else:exit()
    return

def make_sandwiches(ingredient_list) :
    print('샌드위치를 만들겠습니다.')
    for sandwiches_list in ingredient_list:
        print(sandwiches_list+' 추가합니다.')

while True:
    first_message=str(input('''안녕하세요, 저희 가게에 방문해 주셔서 감사합니다.
     1. 주문
     2. 종료
     입력 : '''))

    if (first_message == '1. 주문') or (first_message=='1.주문') or (first_message == '1'):
        input_ingredient()

    elif (first_message == '2. 주문') or (first_message == '2.주문') or (first_message == '2'):
        print('ㅅㄱ')
        break