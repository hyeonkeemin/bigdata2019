# Write a Python program to extract year, month and date from a an url

import re

url = 'http://news.kmib.co.kr/article/view.asp?arcid=0013076716&code=61121111&sid1=soc&cp=nv2'

a = re.compile('[2][\d]\d{2}')
b = re.compile()
year = a.search(url)
month = b.search(url)
print(m)