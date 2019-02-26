import re
original_text = 'life is too short'
p = re.compile('^is')

b=[]
t = p.search(original_text)
b.append(t.group(0))


print(b)