#coding: cp949
age=int(input('���̸� �Է��ϼ��� : '))

if age>0 and age < 4:
    price=0
    grade='����'
elif age >= 4 and age < 14:
    price=2000
    grade='���'
elif age >= 14 and age < 19:
    price=3000
    grade='û�ҳ�'
elif age >= 19 and age < 66:
    price=5000
    grade='����'
elif age >= 66:
    pirce=0
    grade='����'
else:
    print('�ٽ� �Է��ϼ���')
    exit()

if price==0:
    print('���ϴ� %s ����̸�, ����� ���� �Դϴ�.'%grade)
    print('�����մϴ�. Ƽ���� �����մϴ�.')
else:
    print('���ϴ� %s ����̸�, ����� %s �Դϴ�.'%(grade,price))

coast=int(input('����� �Է��ϼ��� : '))
input_price=coast-price

if input_price<0:
    print('%s�� ���ڶ��ϴ�. �Է��Ͻ� %s�� ��ȯ�մϴ�.'%((input_price*-1),coast))
elif input_price>0:
    print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ�մϴ�.'%input_price)
else:
    print('�����մϴ�. Ƽ���� �����մϴ�.')
