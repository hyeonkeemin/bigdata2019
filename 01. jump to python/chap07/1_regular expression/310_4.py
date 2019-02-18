import re
p = re.compile('python', re.MULTILINE)
dest_str='''python one python debug
life is too short
python two
you need python
python three
i will study python'''

m = p.findall(dest_str)
print(m)
