# Write a Python program that matches a string that has an a followed by two to three 'b'.

import re

text = 'abbbb'

m = re.compile('ab{2,3}')
b = m.search(text)

print(b)