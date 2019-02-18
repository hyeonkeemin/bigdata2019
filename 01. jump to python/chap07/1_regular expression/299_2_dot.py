import re
p = re.compile('.....') # \n을 제외한 모든 문자와 매치된다.
m = p.match('1a eZ5')
print(m)