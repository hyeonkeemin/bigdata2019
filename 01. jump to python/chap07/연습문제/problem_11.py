# Write a Python program that matches a word at end of string, with optional punctuation.

import re

text = 'asfklesnfklsnfkBBB_       ff cccb.'

m = re.compile('\w+\S?$')
b = m.search(text)

print(b)

