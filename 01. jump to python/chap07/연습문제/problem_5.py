# Write a Python program that matches a string that has an a followed by three 'b'

import re

text = 'abbbb12333'

m = re.compile('ab{3}')
b = m.search(text)

print(b)