import re

text = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

a = re.compile('(\w+)\s(\d+)[-](\d+)[-](\d+)')
print(a.sub('\g<1> \g<2>-\g<3>-####', text))
