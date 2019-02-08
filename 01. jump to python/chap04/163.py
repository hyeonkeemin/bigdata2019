f=open('./file3.txt', 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')  # 원본에 \n도 있는데 print에도 \n이 기본으로 내장되있으므로 end로 개행 없애줌
f.close()
