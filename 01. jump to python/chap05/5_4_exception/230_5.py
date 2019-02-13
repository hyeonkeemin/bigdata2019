try:
    result = 4/2
    print(result)
    f = open('NA.txt','r')
    f.close()
except Exception as e:
    print(e)

print('program end')

# 모든 Failure를 동일하게 처리하고 싶고 exception의 유형을 정확히 모를때 유용함(일반적인 상황에서 적용가능한 팁)


result = system_cal() #이라는 함수가 있다고 가정

if result == -1:
    print('~ 에러 발생')
    exit()
else:
    print(result)

if result == -1:
    print('에러발생')
    exit()
else
    print(result)
print('program end')

# 다른 언어에서는 예외 처리를 하려면 이것처럼 해야하는데, 파이썬에선 위에 코드처럼 처리하면됨 -> 코드가 간편