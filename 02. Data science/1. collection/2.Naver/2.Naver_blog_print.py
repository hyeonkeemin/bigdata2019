import urllib.request
import datetime
import json

app_id = 'L4zqW8D9OZdRY9ppb4pH'
app_pw = 'zWWm99nCP_'


def get_request_url(url):
    req=urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id',app_id)
    req.add_header('X-Naver-Client-Secret',app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url : %s => Request Success' % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
        return None


def getNaverSearchResult(sNode, search_text, page_start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = '/%s.json' % sNode
    parameters = '?query=%s&start=%s&display=%s' % (urllib.parse.quote(search_text), page_start, display)
    url = base+node+parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)


def getPostData(post,jsonResult):
    title = post['title']
    description = post['description']
    bloggerlink = post['bloggerlink']
    bloggername = post['bloggername']
    link = post['link']

    pDate = datetime.datetime.strptime(post['postdate'], '%Y-%m-%d')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title': title, 'description': description, 'bloggerlink':bloggerlink, 'bloggername':bloggername, 'postdate':pDate})
    return


def main():
    jsonResult = []

    sNode = 'blog'
    search_text = input('검색어를 입력하세요 : ')
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    index = 1 # 1번루프를 돌 때마다 100건이 조회되기 대문에 1000번을 넘기지 않게 하기 위한 인덱스
    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index < 10):
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

        nStart = jsonSearch['start']+jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        index = index + 1

    with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED' % (search_text, sNode))

if __name__ == '__main__':
    main()