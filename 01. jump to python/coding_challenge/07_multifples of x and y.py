while True:
    menu=str(input('''프로그램 시작 : 1, 종료 : 0
    입력 : '''))
    if menu == '1':
        X = int(input('공배수 첫번째(X) : '))
        Y = int(input('공배수 두번째(Y) : '))
        Z = int(input('범위(Z) : '))
        input_range = range(1, Z)
        base_num = 0
        for i in input_range:
            if i % X == 0 or i % Y == 0:
                base_num += i
        print(base_num)
    elif menu == '0':
        break
2
