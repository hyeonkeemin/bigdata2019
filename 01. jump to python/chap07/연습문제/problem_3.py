# Write a Python program that matches a string that has an a followed by one or more b's.

import re

text = 'ab'

m = re.compile('ab+')
b = m.search(text)

print(b)