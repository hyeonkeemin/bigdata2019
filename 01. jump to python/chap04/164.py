f=open('./file3.txt', 'r', encoding='UTF-8')
lines=f.readlines()
# 모든 라인을 리스트에 저장함
# for line in lines:
#     print(line, end='')
print(lines)
f.close()

