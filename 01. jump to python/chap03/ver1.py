#coding: cp949
age=int(input('���̸� �Է��ϼ��� : '))
price=str()
if age < 4:
    price='����'
elif age >= 4 and age < 14:
    price='2000��'
elif age >= 14 and age < 19:
    price='3000��'
elif age >= 19 and age < 66:
    price='5000��'
else:
    pirce='����'
print('����� %s �Դϴ�.'%price)
