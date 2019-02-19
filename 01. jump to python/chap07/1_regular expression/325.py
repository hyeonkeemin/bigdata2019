import re

# 이름 + 전화번호 문자열을 전화번호 + 이름으로 바꾸기
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub('\g<phone> \g<name>','park 010-1234-5678'))

# 그룹명 대신 참조번호를 써도 마찬가지당
print(p.sub('\g<2> \g<1>','park 010-1234-5678'))
