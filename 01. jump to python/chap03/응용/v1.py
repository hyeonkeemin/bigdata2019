#encoding:cp949
while True:
    num = int(input('홀수를 입력하세요(0 <- 종료) : '))
    if not num:
        print('안뇽');break
    elif num % 2 == 0:
        print("다시 입력하세요");continue
    else:
        for star in range(1,num,2):
            print(star)
