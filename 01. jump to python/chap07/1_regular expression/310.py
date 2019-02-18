import re
p = re.compile('^python\s\w+', re.MULTILINE) # ^python~ : python 으로 시작되는 문자열 매치
dest_str='''python one python debug
life is too short
python two
you need python
python three'''

m = p.findall(dest_str)
print(m)