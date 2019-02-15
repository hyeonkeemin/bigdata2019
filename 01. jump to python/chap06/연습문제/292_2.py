def dup_num(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

a=str(input('수 입력 : '))
print(dup_num(a))