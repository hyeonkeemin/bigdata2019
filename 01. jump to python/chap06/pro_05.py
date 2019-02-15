def my_calculator():
    while True:
        menu = str(input('계산 유형을 선택하세요(1:덧셈 2:뺄셈 3:곱셈 4:나눗셈. 0:종료) : '))
        if menu == '0':
            break
        num1, num2 = str(input('두 수를 입력하세요(공백으로 구분) : ')). split()
        try:
            try:
                int(num1)
            except ValueError :
                print('첫번째 입력이 \'%s\' 입니다. 다시 입력하세요.\n'%num1)
            try:
                int(num2)
            except ValueError:
                print('두번째 입력이 \'%s\' 입니다. 다시 입력하세요.\n'%num2)

            if menu == '1':
                result = int(num1) + int(num2)
                print(result,'\n')
            elif menu == '2':
                result = int(num1) - int(num2)
                print(result, '\n')
            elif menu == '3' :
                result = int(num1) * int(num2)
                print(result, '\n')
            elif menu == '4' :
                try:
                    int(num1) / int(num2)
                    result = int(num1) / int(num2)
                    print(result, '\n')
                except ZeroDivisionError:
                    print('죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.\n')

        except:
                continue


my_calculator()


