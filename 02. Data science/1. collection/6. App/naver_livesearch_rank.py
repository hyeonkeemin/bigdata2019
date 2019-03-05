from bs4 import BeautifulSoup
import re
import urllib.request
import csv

def naver_livesearch_rank():
    html = urllib.request.urlopen('https://www.naver.com')
    soup = BeautifulSoup(html, 'html.parser')

    tag = str(soup)

    search_type = re.compile('"ah_k">(.+)</span>')
    search_list = search_type.findall(tag)

    print('\n<<< 네이버 실시간 검색어 순위 >>>')
    for i in range(20):
        print(str(i+1)+'위: '+search_list[i])


    f = open('live_ranking_search_info.csv', 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['순위', '검색어'])
    for i in range(20):
        csv_writer.writerow([i+1, search_list[i]])
    print('\n"live_ranking_search_info"에 실시간 검색어 순위 정보를 csv 형태로 저장하였습니다.')

if __name__ == '__main__':
    naver_livesearch_rank()
