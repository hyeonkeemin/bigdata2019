def read_content():
    try:
        with open('./poll.txt', 'r', encoding='UTF-8') as a:
            print(a.read())

    except FileNotFoundError:
        f_not = str(input('''기존 poll.txt파일을 찾을 수 없습니다. 아래 중 선택하세요.
            1. 종료 2. 새로운 파일 생성 3. 변경된 파일 경로 입력 : '''))

        if f_not == '1':
            exit()

        elif f_not == '2':
            from pro_02 import survey
            survey()
            b = open('./poll.txt', 'r', encoding='UTF-8')
            print('<현재 누적 응답 현황 >', '\n' + b.read())
            b.close()

        elif f_not == '3':
            direct = str(input('변경된 파일 경로를 입력하세요 : '))
            while True:
                question = str(input('프로그래밍이 왜 좋으세요? (종료 입력시 종료) : '))
                if question == '종료':
                    break
                else:
                    name = str(input('이름을 입력하세요 : '))
                    print('설문에 응답해주셔서 감사합니다.')

                    exist_poll = open('./backup/poll.txt', 'r',encoding='UTF-8')
                    exist_poll_read = exist_poll.read()
                    exist_poll.close()

                    poll = open('%s/poll.txt'%direct, 'a', encoding='UTF-8')
                    poll.write(exist_poll_read)
                    poll.write('[%s] ' % name + question + '\n')
                    poll.close()
            c = open('%s/poll.txt'%direct, 'r', encoding='UTF-8')
            print('<현재 누적 응답 현황 >', '\n' + c.read())
            c.close()

read_content()



