a = '이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌'
b_kim = 0
b_lee = 0
for i in a:
    if i[0] == '김':
        b_kim += 1
    elif i[0] == '이':
        b_lee += 1

print('김씨 수 : ', b_kim)
print('이씨 수 : ', b_lee)
print('이재영 이름 수 : ', a.count('이재영'))

b = list(set(a))
print(b)
print(sorted(b))
