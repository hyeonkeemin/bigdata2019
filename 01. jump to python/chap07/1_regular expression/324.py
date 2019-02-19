import re
p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))

print(p.sub('color', 'blue socks and red shoes', count=1)) # 횟수를 제어하려면 뒤에 count를 붙여준당





