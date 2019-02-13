try:
    f = open('foo.txt', 'r')
    result=4/0
    except FileNotFoundError as e:
    print(e)

print('progress end')
f.close()
