#coding: cp949
age=int(input('나이를 입력하세요 : '))
price=int()
grade=str()
if age>0 and age < 4:
    price=0
    grade='유아'
elif age >= 4 and age < 14:
    price=2000
    grade='어린이'
elif age >= 14 and age < 19:
    price=3000
    grade='청소년'
elif age >= 19 and age < 66:
    price=5000
    grade='성인'
elif age >= 66:
    pirce=0
    grade='노인'
else:
    print('다시 입력하세요')
    exit()

if price==0:
    print('귀하는 %s 등급이며, 요금은 무료 입니다.'%grade)
else:
    print('귀하는 %s 등급이며, 요금은 %s 입니다.'%(grade,price))


