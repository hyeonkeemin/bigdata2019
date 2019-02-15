                                            # a a a b b c a
                                            # 0 1 2 3 4 5 6
def check():
    input_string = list(input('입력 : '))
    new_string = []
    cnt = 0
    i = 0
    j = -1
    while j <= len(input_string):
        j += 1
        cnt += 1
        if j == len(input_string):
            break
        if input_string[i] != input_string[j]:
            i = j
            new_string.append(input_string[i-1]+str(cnt))
            cnt = 0
    print(new_string)

check()
