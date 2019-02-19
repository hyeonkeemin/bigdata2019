# Write a Python program to find sequences of one upper case letter followed by lower case letters

import re

text = '    Dssadfsfesfs  '

m = re.compile('[A-Z][a-z]*')
b = m.search(text)

print(b)