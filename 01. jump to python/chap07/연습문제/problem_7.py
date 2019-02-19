# Write a Python program to find sequences of lowercase letters joined with a underscore

import re

text = 'abbbdd_bfefef'

m = re.compile('^[a-z]+_[a-z]+$')
b = m.search(text)

print(b)