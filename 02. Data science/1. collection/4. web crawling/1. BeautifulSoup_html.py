# 웹 페이지를 가져오고 분석하는 외부 모듈
#pip install bs4
from bs4 import BeautifulSoup

html = """
<html>
네이버 실시간 영화 순위
<td class='title'>
<div class='tit3'>
<a href='/movie/bi/mi/basic.nhn?code=158191' title='1위 영화' >극한직업
</a>
</div>
</td>
</html>
"""

# 태그 접근
soup = BeautifulSoup(html,'html.parser')

print(soup)
tag = soup.td
print('\nsoup.td')
print(tag)

tag = soup.div
print('\nsoup.div')
print(tag)

tag=soup.a
print('\nsoup.a')
print(tag)

# 태그 확인
print('\ntag.name')
print(tag.name)

print('\ntag.attrs') # 값이 여러개일 경우 딕셔너리로 반환
print(tag.attrs)

print('\ntag.text')
print(tag.text)

print('\ntag.string')
print(tag.string)