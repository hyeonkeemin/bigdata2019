# Write a Python program that matches a string that has an a followed by zero or more b's.

import re

text = 'abb'

m = re.compile('ab*')
b = m.search(text)

print(b)