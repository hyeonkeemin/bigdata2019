import re
a = re.compile('a[.]{3,}b')
m = 'a....b'

print(a.match(m))