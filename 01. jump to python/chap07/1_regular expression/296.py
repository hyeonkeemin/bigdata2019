data='''
park 800905-1049118
kim 700905-1059119
'''

result=[]
for line in data.split('\n'):
    word_result=[]
    for word in line.split(' '): # 공백 문자마다 나누기
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+'-'+'*******'
        word_result.append(word)
    result.append(' '.join(word_result)) # 나눈 단어 조립하기
print('\n'.join(result))