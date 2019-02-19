# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

# text_kind_list=['a','A','1','!','@','#','$','%','^','&','*','(',')','-','_','<','>','/','?','"',':',';','+',',','`','~']
# for char_sample in text_kind_list:
#     sample = re.compile('\w')
#     result = sample.search(char_sample)
#     print(result)

text = 'asfkleseeenfzk______snfkBBB       ff cccb'

m = re.compile('[\w]+')
b = m.search(text)

print(b)

