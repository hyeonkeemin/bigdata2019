# Write a Python program where a string will start with a specific number.

import re

text = '11-f23132zxfvv'

m = re.compile('^\d+[-]\w+')
b = m.search(text)

print(b)