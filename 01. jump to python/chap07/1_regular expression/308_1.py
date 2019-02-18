import re
original_text = 'a\nb'
# p = re.compile('a.b')
p = re.compile('a.b', re.DOTALL)
m = p.match(original_text)
print(m)
