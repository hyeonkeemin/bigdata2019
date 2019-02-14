def read_content():
    try:
        a = open('./poll.txt','r',encoding='UTF-8')
    except FileNotFoundError:
        f_not = str(input('''기존 poll.txt파일을 찾을 수 없습니다. 아래 중 선택하세요.
            1. 종료 2. 새로운 파일 생성 3. 변경된 파일 경로 입력 : '''))
        while True:
            if f_not == '1':
                break

            elif f_not == '2':
               from pro_02 import survey
               survey()
               b = open('poll.txt', 'r', encoding='UTF-8')
               b.read()
               b.close()

            elif f_not == '3':
                direct = str(input('파일 경로를 입력하세요 : '))
                c = open('%s'%direct, 'a', encoding='UTF-8')






