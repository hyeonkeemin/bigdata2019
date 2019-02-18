import re
original_text = 'life is too short'
p = re.compile('[a-z]+')

result = p.finditer(original_text) # 매칭된 결과를 'match object' 리스트로 반환
for r in result:
    print(r)