# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re

text = '    AaA123bBb456 '

m = re.compile('\w+')
b = m.search(text)

print(b)