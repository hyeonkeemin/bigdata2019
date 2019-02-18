import re
p = re.compile('crow|servo')

m = p.match('nothing') # 안매칭
print(m)
m=p.match('crow') # 매칭
print(m)
m=p.match('servo') # 매칭
print(m)
m=p.match('crowservo') # 매칭
print(m)

