def my_sum(a,b):
    return a+b

a=3
b=4
print(my_sum(3,4))

def my_say():
    return 'Hi'

print(my_say())

# 여러개의 입력값
def multi_sum(*args):
    sum=0
    for i in args:
        sum = sum + i
    return sum

result=multi_sum(1,2,3,6)
print(result)

def sum_mul(choice,*args):
    if choice == 'sum':
        result=0
        for i in args:
            result+=i
    elif choice == 'mul':
        result=1
        for i in args:
            result*=i
    return result

result=sum_mul('sum', 1,2,3,4,5,6,7,8,9,10)
print(result)
result=sum_mul('mul', 1,2,3,4,5)
print(result)

print('')

ac=1
def v(ac):
    ac=ac+1
    return ac
v(ac)
print(ac)

