import time
from scipy import stats
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score

# 빅데이터
# InvoiceNo : 6자리 숫자로 이루어진 거래 고유번호
# StockCode : 5자리 숫자로 이루어진 상품 코드
# Description : 상품명
# Quantity : 한 거래당 판매된 상품 수
# InvoiceDate : 거래가 성립된 일시 MM/DD/YY HH:MM
# UnitPrice : 가격
# CustomerID : 사용자 ID
# Country : 사용자의 국가

# 데이터의 구조 정의
# 사용자 ID를 키로, 상품 코드의 셋을 벨류로 갖는 딕셔너리
user_product_dic = {}
# 상품 코드를 키로, 사용자 ID의 셋을 벨류로 갖는 딕셔너리
product_user_dic = {}

# 상품 코드를 키로 가지고 상품명을 벨류로 갖는 딕셔너리
# 군집화의 내용을 확인하는 단계에서 상품명을 사용합니다.
product_id_name_dic = {}

def analyze_clusters_keyword(labels, product_id_name_dic, user_product_dic, id_user_dic):
    # 각 클러스터의 아이디와, 해당 아이디의 클러스터 들어 있는 유저 수를 출력
    print(Counter(labels)) # 리스트의 각각의 값 별로 누적 현황 확인
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])

        # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
        # 그 사용자 코드와 연결된 구매 상품의 ID를 참조한 후
        # 그 ID를 이용해 상품명을 찾아
        # 딕셔너리에 클러스터 ID를 키로, 상품명을 값으로 추가
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        # 각 클러스터안의 상품명을 join 명령으로 합쳐 하나의 문자열로 만든 뒤
        # 스페이스 혹은 탭으로 스플릿하여 키워드로 분해
        product_name_keyword = (' ').join(product_name).split()

        # 클러스터의 아이디와, 그 아이디를 가지는 클러스터에 속하는 유저들이 구매한 상품들의 상품명안에
        # 가장 자주 나타나는 단어 20개를 역순으로 출력
        print('cluster_id : ', cluster_id)
        print(Counter(product_name_keyword).most_common(20))


def analyze_clusters_keyword_bigram(labels, product_id_name_dic, user_product_dic, id_user_dic):
    # 각 클러스터의 아이디와, 해당 아이디의 클러스터에 들어있는 유저 수를 출력
    print(Counter(labels))
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])

        # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
        # 그 사용자 코드와 연결된 구매상품의 ID를 참조한 후
        # 그 ID를 이용해 상품명을 찾아
        # 딕셔너리에 클러스터 ID를 키로, 상품명을 값으로 추가
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        # 각 클러스터 안의 상품명을 join 명령으로 합쳐 하나의 문자열로 만든 뒤
        # OF를 공백으로 리플레이스하고
        # 스페이스 혹은 탭으로 스플릿하여 키워드를 분해한 뒤
        # 연속되는 두 키워드를 합쳐서 하나의 키워드를 생성
        bigram = []
        product_name_keyword = (' ').join(product_name).replace(' OF ', ' ').split()
        for i in range(0, len(product_name_keyword) - 1):
            bigram.append(' '.join(product_name_keyword[i:i + 2]))
        print('cluster_id:', cluster_id)
        print(Counter(bigram).most_common(20))

def analyze_clusters_product_count(labels, user_product_dic, id_user_dic):
    product_len_dic = {}

    for i in range(0, len(labels)):
        product_len_dic.setdefault(labels[i], [])

        product_len_dic[labels[i]].append(len(user_product_dic[id_user_dic[i]]))

    for k, v in product_len_dic.items():
        print('clusters : ', k)
        print(stats.describe(v))

# 파일을 읽어 위에 정의한 데이터 구조를 채움
for line in open('online_retail_utf.txt'):

    # 데이터를 한 행씩 읽어서 필요한 항목을 저장
    line_items = line.strip().split('\t')
    user_code = line_items[6]
    product_id = line_items[1]
    product_name = line_items[2]

    # 사용자 ID가 없을 경우 무시합니다.
    if len(user_code) == 0:
        continue

    # 영국에서 구매한 사용자를 고려합니다.
    country = line_items[7]
    if country != 'United Kingdom':
        continue

    # 연도 읽을때 에러 처리, 파일 헤더 무시
    try:
        invoice_year = time.strptime(line_items[4], '%m/%d/%y %H:%M').tm_year
    except ValueError:
        continue

    # 2011년에 읽어난 구매가 아닌 것은 무시
    if invoice_year != 2011:
        continue

    # 읽은 정보로 데이터 구조를 채움
    # 상품 가짓수를 고려하므로 상품 코드를 셋으로 가지도록 할 예정
    user_product_dic.setdefault(user_code, set()) # set의 결과는 공집합 # user_product_dic[user_code] = set() 이랑 같음.
    # ex) {17850: {}} 형식으로 만듬
    user_product_dic[user_code].add(product_id)

    product_user_dic.setdefault(product_id, set())
    product_user_dic[product_id].add(user_code)

    product_id_name_dic[product_id] = product_name

# 데이터 구조를 다 채웠으므로 각 사용자들이 구매한 상품 가짓수로 리스트를 생성
product_per_user_li = [len(x) for x in user_product_dic.values()]

print('Step 1] 빅데이터 로딩 완료')
# 최종 사용자 수와 상품 가짓수를 출력
print(' # of user:', len(user_product_dic))
print(' # of product:', len(product_user_dic))

# 각 사용자들이 구매한 상품 가짓수로 기초 통계량을 출력
print(stats.describe(product_per_user_li))

# 구매한 상품의 가짓수가 1인 사용자의 사용자 ID를 검색
min_product_user_li = [k for k, v in user_product_dic.items() if len(v) == 1]
# 마찬가지로, 구매한 상품의 가짓수가 600개 이상인 사용자의 사용자 ID를 검색
max_product_user_li = [k for k, v in user_product_dic.items() if len(v) >= 600]

print(' # of users purchase')