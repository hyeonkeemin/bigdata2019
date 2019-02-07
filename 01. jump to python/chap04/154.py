a=1 # 전역변수(Global variable)
# 전역변수는 힙(Heap)이라는 메모리 공간에 저장되며 프로그램이 끝날 때 까지 유효하다. 어디에서나 접근가능
def vartest(a):
    a=a+1 # 지역변수(Local variable)
    # 지역변수는 스택(Stack)에 저장되며 함수호출이 끝나면 사라진다. 해당 함수에서만 접근 가능함

vartest(a)

print(a)