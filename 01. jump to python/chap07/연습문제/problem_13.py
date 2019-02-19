# Write a Python program that matches a word containing 'z', not start or end of the word.

import re

text = 'asfkleseeenfzklsnfkBBB_       ff cccb'

m = re.compile('\S+z+\S+')
b = m.search(text)

print(b)