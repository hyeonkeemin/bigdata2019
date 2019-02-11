new_visitor_birth=[]

def search_visitor():
    visitor = open('./방명록.txt', 'r', encoding='UTF-8')
    name = str(input('이름을 입력하세요 : '))
    name_list = visitor.read()

    if name in name_list:
        print('%s님 다시 방문해주셔서 감사합니다. 즐거운 시간 되세요'%name)
        return name

    elif name not in name_list:
        new_visitor_birth=str(input('생년월일을 입력하세요 : '))
        print('''%s님 환영합니다. 아래 내용을 입력하셨습니다.
        '''%name, name, new_visitor_birth)
        input_visitor=open('./방명록.txt', 'a', encoding='UTF-8')
        input_visitor.write('\n'+name)
        input_visitor.write(' '+new_visitor_birth)
        return ''
    visitor.close()

search_visitor()
