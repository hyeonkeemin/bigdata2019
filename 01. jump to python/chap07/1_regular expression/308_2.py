import re
original_text = '''asdklfmsaef
 sadlkfmsef'''

# p = re.compile('[a-z]*. [a-z]*') # 안됨
p = re.compile('[a-z]*. [a-z]*', re.DOTALL) # 됨

m = p.match(original_text)
print(m)