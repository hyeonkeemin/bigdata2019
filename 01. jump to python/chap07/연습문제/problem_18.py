# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re

text = 'exercises number 1, 12, 13, and 345 are important'
a = re.compile('[\d]+')
m = a.findall(text)
print(m)
