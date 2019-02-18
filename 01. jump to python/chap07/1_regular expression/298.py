import re #정규식을 표현하기 위한거

p = re.compile('[abc]')

a = p.match('a')
b = p.match('k')
c = p.match('before')
d = p.match('dude')
e = p.match('bca')

print(a) # 매칭이 됨
print(b) # 매칭이 안됨
print(c)
print(d)
print(e)

# [ ] 안의 글자는 저거 셋 중에 아무거나 하나가 될 수 있다는 뜻.
p = re.compile('[abc]')
m = p.match('dad')
print(m) # 첫번째 글자에 abc가 없어서 매칭이 안된다. 두번째 글자가 문자열 클래스에 있으나 첫번째가 아니기 때문에 매칭이 안됨
p = re.compile('d[def]')
m = p.match('dad')
print(m) # 매칭안됨. 두번째 글자에 a가 없어서 ㄴㄴ
p = re.compile('d[abc]')
m = p.match('dad')
print(m) # 매칭됨. da 반환
p = re.compile('d[abc]a')
m = p.match('dad')
print(m) # 매칭안됨. 세글자가 매칭되어야 하는데 중간에 abc여야 하는 조건.
p = re.compile('[abc]d')
m = p.match('dad')
print(m) # 매칭안됨. 첫글자 조건이 abc인데 d임
p = re.compile('[cd][ab]')
m = p.match('da')
print(m) # 매칭됨. 첫번째 글자에 d에 해당 두번째 글자에 a 해당
