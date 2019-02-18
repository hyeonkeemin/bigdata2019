import re
p = re.compile('[a-z]+')
m = p.search('3 python')
# m = p.match('python')
print(m)

if m:
    print('match found:',m.group())
else:
    print('no match')