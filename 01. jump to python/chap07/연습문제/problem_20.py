# Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'

import re

text = 'The quick brown fox jumps over the lazy dog.'
a = re.compile('fox')
m = a.search(text).group()
print(text.find(m))
