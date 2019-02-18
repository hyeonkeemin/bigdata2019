import re
p = re.compile('[\d][\D][\s][\S][\w][\W]')
m = p.match('1a !G  ')
print(m)