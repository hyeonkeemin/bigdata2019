# Write a Python program to find the occurrence and position of the substrings within a string.

import re

text = 'Python_exercises, PHP_exercises, C#_exercises'
a = re.sub('\s', '_', text)
b = re.sub('_', ' ', text)
# m = a.findall(text)
print(a)
print(b)
