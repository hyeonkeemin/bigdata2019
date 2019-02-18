import re
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('paris in the the spring.').group())

print(p.findall('paris in the the spring. it it was really great'))
