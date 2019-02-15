def survey():
    while True:
        question = str(input('프로그래밍이 왜 좋으세요? (종료 입력시 종료) : '))
        if question == '종료':
            break
        else:
            name = str(input('이름을 입력하세요 : '))
            print('설문에 응답해주셔서 감사합니다.')
            poll = open('poll.txt', 'a', encoding='UTF-8')
            poll.write('[%s] '%name + question+'\n')
            poll.close()


if __name__ == '__main__':
    survey()
