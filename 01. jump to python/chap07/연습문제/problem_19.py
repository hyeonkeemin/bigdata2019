# Write a Python program to search some literals strings in a string
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

import re

text = 'The quick brown fox jumps over the lazy dog.'
a = re.compile('fox|dog|horse')
m = a.findall(text)
print(m)
