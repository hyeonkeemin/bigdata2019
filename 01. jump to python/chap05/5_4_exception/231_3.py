try:
    denominator = int(input('분모 입력 : '))
    print('progress 1')
    f=open('foo.txt','r')
    print('progress 2')
    result=4/denominator
    print('progress 3')
    f.close()
    print('progress 4')
except Exception as e:
    print(e)
