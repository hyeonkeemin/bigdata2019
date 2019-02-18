import re
p = re.compile('.+(?=:)') # http 다음 ' : '가 표시되지 않게함
m = p.search('http://google.com')
print(m.group())