#coding: cp949
age=int(input('나이를 입력하세요 : '))

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
    print('감사합니다. 티켓을 발행합니다.')
else:
    print('귀하는 %s 등급이며, 요금은 %s 입니다.'%(grade,price))

coast=int(input('요금을 입력하세요 : '))
input_price=coast-price

if input_price<0:
    print('%s가 모자랍니다. 입력하신 %s를 반환합니다.'%((input_price*-1),coast))
elif input_price>0:
    print('감사합니다. 티켓을 발행하고 거스름돈 %s를 반환합니다.'%input_price)
else:
    print('감사합니다. 티켓을 발행합니다.')
