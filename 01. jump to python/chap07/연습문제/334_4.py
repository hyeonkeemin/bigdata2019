email_list = ['park@naver.com', 'kim@daum.net','lee@myhome.co.kr']

import re

v1 = re.compile('\w+[@]+\w+[.]((?!com|net))')
for i in email_list:
    a = v1.search(i)
    print(a)