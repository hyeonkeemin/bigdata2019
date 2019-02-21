a = [['1','2',['3','4'],'aa'],['3','4',['aa','bb'],'cc']]

import re
m = re.compile(input('입력 : '))
b = m.search(a)

if b in a:
    print('god')

