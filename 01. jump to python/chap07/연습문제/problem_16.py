# Write a Python program to remove leading zeros from an IP address.

import re

text = '120.08.016.300.1.23'

# m = re.sub('\.[0]*', '.', text)
# b = m.search(text)

# print(m)

t = re.compile('\.(?=2)\d+')
r = t.findall(text)
print(r)