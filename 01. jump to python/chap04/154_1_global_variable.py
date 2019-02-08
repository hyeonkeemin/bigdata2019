a=1 # 전역변수
def global_var_read():
    print(a)
def global_var_write():
    a+=2 # 변수에 값을 쓰려는 순간 파이썬에서는 변수를 지역변수로 인식한다. 따라서 a+=2는 문법적으로 오류

def global_var_write2():
    global a # 전역변수 a를 함수 안에서 값을 쓰고자 할 때 문법상 선언함
    a+=2

global_var_read()
print(a)

# global_var_write() 호출하면 에러가 발생한다
global_var_write2()
print(a)