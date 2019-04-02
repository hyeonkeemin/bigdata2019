import codecs
from konlpy.tag import Okt

# 파일 열고 글자 출력
fp = codecs.open('hong.txt', 'r', encoding='utf-8')
text = fp.read()

# 텍스트 한줄씩 처리
okt = Okt()
word_dic = {}
lines = text.split('\r\n')
# print(lines)

for line in lines:
    malist = okt.pos(line)
    for word in malist:
        if word[1] == 'Noun': # 명사 확인하기
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1

# 많이 사용된 명사 출력
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print('{0}({1})'.format(word, count), end='')
print()