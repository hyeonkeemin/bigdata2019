#encoding:cp949
while True:
    num = int(input('Ȧ���� �Է��ϼ���(0 <- ����) : '))
    if not num:
        print('�ȴ�');break
    elif num % 2 == 0:
        print("�ٽ� �Է��ϼ���");continue
    else:
        for star in range(1,num,2):
            print(star)
