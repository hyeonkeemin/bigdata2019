#coding: cp949
age=int(input('나이를 입력하세요 : '))
price=str()
if age < 4:
    price='무료'
elif age >= 4 and age < 14:
    price='2000원'
elif age >= 14 and age < 19:
    price='3000원'
elif age >= 19 and age < 66:
    price='5000원'
else:
    pirce='무료'
print('요금은 %s 입니다.'%price)
