#coding: cp949
enter_num=0
free_ticket=3
sale_ticket=5

while True:
    
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
        price=0
        grade='����'
    else:
        print('�ٽ� �Է��ϼ���')
        continue

    if price==0:
        print('���ϴ� %s ����̸�, ����� ���� �Դϴ�.'%grade)
        print('�����մϴ�. Ƽ���� �����մϴ�.',)
        continue
        
    else:
        print('���ϴ� %s ����̸�, ����� %s �Դϴ�.'%(grade,price))
        
    payment=int(input('��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��) : '))      


    
    if payment==1:
        coast=int(input('����� �Է��ϼ��� : '))
        input_price=coast-price

        if input_price>0:
            print('�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s�� ��ȯ�մϴ�.'%input_price)
            
        elif input_price<0:
            print('%s���� ���ڶ��ϴ�. �Է��Ͻ� %s���� ��ȯ�մϴ�.'%((input_price*-1),coast))    
            continue

        else:
            print('�����մϴ�. Ƽ���� �����մϴ�.')


    elif payment==2 and age<60:
        print('%s�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.'%(price*0.9))

    else:
        print('%s�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.'%((price*0.9)*0.95))

    enter_num += 1
    print('����Ƚ�� : ',enter_num)
    
    if enter_num % 7 == 0:
        free_ticket -= 1
        print('�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� [%d��]'%(free_ticket))
        if free_ticket == 0:
            continue
    if enter_num % 4 == 0:
        sale_ticket -= 1
        print('"�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� [%d]��'%sale_ticket)
        if sale_ticket == 0:
            continue

    if not free_ticket and sale_ticket:
        break
