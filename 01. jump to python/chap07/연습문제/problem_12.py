# Write a Python program that matches a word containing 'z'

import re

text = 'asfklesnfzklsnfkBBB_       ff cccb.'

m = re.compile('z')
b = m.search(text)

print(b)