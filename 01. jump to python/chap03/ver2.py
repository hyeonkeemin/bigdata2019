#coding: cp949
age=int(input('���̸� �Է��ϼ��� : '))
price=int()
grade=str()
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
else:
    print('���ϴ� %s ����̸�, ����� %s �Դϴ�.'%(grade,price))


