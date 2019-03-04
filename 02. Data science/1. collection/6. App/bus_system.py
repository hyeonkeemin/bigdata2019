import urllib.request, datetime, json, time


access_key = 'fDy2oV4J0d1lZaHHVGaBMJrdZisptaAUNaSm4cF9Gc9D7GWTGiD20dAYMJwlUEs6keAZgoZpBLQpzYNo5KVTYg%3D%3D'

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
           print("[%s] Url Request Success" %datetime.datetime.now())
           return response.read().decode("UTF-8")
    except Exception as e :
        print(e)
        print(" [%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def get_Bus_URL(url) :
    end_point = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getSttnNoList'

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&cityCode="+cityCode
    parameters += '&nodeNm='+nodeNm

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None) :
        return None
    else :
        return json.loads(retData)


def Make_ID_Json():
    jsonData = get_Request_URL()

    if (jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE') :
        for prn_data in jsonData['response']['body']['items']['item'] :
            json_bus_result.append({'nodeid': prn_data['nodeid'], 'nodenm': prn_data['nodenm']})


def get_Bus_info():
    return




json_bus_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
cityCode = str(22)
nodeNm = str(input('확인할 버스 정류장을 입력하세요 : '))

# if __name__ == "__main__" :
