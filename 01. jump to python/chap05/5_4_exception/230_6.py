input_denominator = int(input('분모를 입력하시오 : '))

try:
    result = 4/input_denominator
    print(result)

    f=open('NA.txt', 'r')
    f.close()

except ZeroDivisionError as e:
    print(e)
    print('분모가 0이 되면 안됨. 다시 입력')

except FileNotFoundError as e:
    print(e)
    print('해당 파일이 존재하지 않음')

print('program end')