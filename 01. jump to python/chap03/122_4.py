#coding: cp949
feel ='ȣ��'
hit_on_count=0

while feel:
    hit_on_count += 1 #1�� ������
    print('%d�� ����Ʈ ��û�մϴ�.'%hit_on_count)
    if hit_on_count == 10:
        print('����� ���� �ٰ� �Գ׿�.')
        continue
    feel=input('���� �׳࿡ ���� ����� ������ �����?')
    if(feel=='��ȣ��'):
        print('�׷� �ܳ��ϼ���')
        break

