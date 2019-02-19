# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

import re

text = 'asfklesnfklsnfkBBB_         b'

m = re.compile('^a.*b$')
b = m.search(text)

print(b)