from bs4 import BeautifulSoup
import re
import urllib.request

def naver_livesearch_rank():
    html = urllib.request.urlopen('https://www.naver.com')
    soup = BeautifulSoup(html, 'html.parser')

    tag = str(soup)

    search_type = re.compile('"ah_k">(.+)</span>')
    search_list = search_type.findall(tag)

    print('\n<<< 네이버 실시간 검색어 순위 >>>')
    for i in range(20):
        print(str(i+1)+'위: '+search_list[i])

if __name__ == '__main__':
    naver_livesearch_rank()
