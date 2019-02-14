                           'aaaabbc'
def new_a(input_str):
    cnd = 0
    list_output = list(input_str)
    for output_str in input_str:
        a



new_a('aaabb')




















def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print (compress_string("aaabbcccccca"))