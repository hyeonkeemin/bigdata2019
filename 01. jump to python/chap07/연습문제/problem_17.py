# Write a Python program to remove leading zeros from an IP address.

import re

text = '120.08.016.300 efawsfsf4'

a = re.compile('\w+[0-9]$')
m = a.search(text)
print(m)