# Write a Python program that matches a string that has an a followed by zero or one 'b'.

import re

text = 'abbbbbbbbbbbbbbbbbbbbbbb'

m = re.compile('ab?')
b = m.search(text)

print(b)