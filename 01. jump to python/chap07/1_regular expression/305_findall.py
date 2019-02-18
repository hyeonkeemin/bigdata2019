import re
original_text = 'life is too short'
p = re.compile('[a-z]+')

m=p.search(original_text) # search는 맨 앞에꺼만 찾아줌
print(m)

m=p.findall(original_text) # findall은 다 찾아줌. 매칭된 문자열들을 리스트로 반환
print(m)