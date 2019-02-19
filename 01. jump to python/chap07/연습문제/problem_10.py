# Write a Python program that matches a word at the beginning of a string.

import re

text = 'asfklesnfklsnfkBBB_         b'

m = re.compile('^\w.*')
b = m.search(text)

print(b)