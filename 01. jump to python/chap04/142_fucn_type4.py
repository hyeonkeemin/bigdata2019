# 입력(parameter), 출력(return)이 있는 함수

def my_sum():
    num1, num2 = input('두 수 입력하시오 : ').split()
    num1=int(num1)
    num2=int(num2)
    return num1+num2

result=my_sum()
print(result)