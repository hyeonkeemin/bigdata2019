# Write a Python program to find the occurrence and position of the substrings within a string.

import re

text = 'Python exercises, PHP exercises, C# exercises'
a = re.compile('.+\sexercises')
m = a.findall(text)
print(m)
