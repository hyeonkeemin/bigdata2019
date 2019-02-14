                            # 123156
def duplicate():
    input_num = str(input('숫자 입력하세요 : '))
    result = []
    result_dup = []
    if len(input_num) < 10:
        result_dup = False
    else:
        for num in input_num:
            result.append(num)
            if num not in result:
                result_dup = True
            else:
                result_dup = False
    print(result_dup)

duplicate()




