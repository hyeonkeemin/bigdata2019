#coding: cp949
enter_num=0
free_ticket=3
sale_ticket=5

while True:
    
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
        price=0
        grade='노인'
    else:
        print('다시 입력하세요')
        continue

    if price==0:
        print('귀하는 %s 등급이며, 요금은 무료 입니다.'%grade)
        print('감사합니다. 티켓을 발행합니다.',)
        continue
        
    else:
        print('귀하는 %s 등급이며, 요금은 %s 입니다.'%(grade,price))
        
    payment=int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드) : '))      


    
    if payment==1:
        coast=int(input('요금을 입력하세요 : '))
        input_price=coast-price

        if input_price>0:
            print('감사합니다. 티켓을 발행하고 거스름돈 %s를 반환합니다.'%input_price)
            
        elif input_price<0:
            print('%s원이 모자랍니다. 입력하신 %s원을 반환합니다.'%((input_price*-1),coast))    
            continue

        else:
            print('감사합니다. 티켓을 발행합니다.')


    elif payment==2 and age<60:
        print('%s원 결제 되었습니다. 티켓을 발행합니다.'%(price*0.9))

    else:
        print('%s원 결제 되었습니다. 티켓을 발행합니다.'%((price*0.9)*0.95))

    enter_num += 1
    print('결제횟수 : ',enter_num)
    
    if enter_num % 7 == 0:
        free_ticket -= 1
        print('축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료티켓을 발행합니다. 잔여 무료티켓 [%d장]'%(free_ticket))
        if free_ticket == 0:
            continue
    if enter_num % 4 == 0:
        sale_ticket -= 1
        print('"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 [%d]장'%sale_ticket)
        if sale_ticket == 0:
            continue

    if not free_ticket and sale_ticket:
        break
