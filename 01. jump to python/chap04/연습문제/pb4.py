visitor = open('./방명록.txt', 'r', encoding='UTF-8')

visitor_info = visitor.readlines()

def search_visitor():
    name = str(input('이름을 입력하세요 : '))
    while True:
        if name in visitor_info:
            print('%s 님 방문해주셔서 감사합니다.'%name)
            return name
        elif name in visitor_info:
            print('없다')
            return ''

search_visitor()

visitor.close()