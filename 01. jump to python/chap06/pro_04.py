def my_sum():
    while True:
        try:
            num1, num2 = str(input('두 수를 입력하세요(종료: 프로그램 종료) : ')). split()
        except ValueError:
                break
        try:
            try:
                int(num1)
            except ValueError :
                print('첫번째 입력이 %s 입니다. 다시 입력하세요.'%num1)
            try:
                int(num2)
            except ValueError:
                print('두번째 입력이 %s 입니다. 다시 입력하세요.'%num2)
            result = int(num1) + int(num2)
            print(result)
        except:
            continue
my_sum()

