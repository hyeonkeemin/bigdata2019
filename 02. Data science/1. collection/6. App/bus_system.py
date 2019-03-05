import urllib.request, datetime, json, time
import xml.etree.ElementTree as ET
import csv

access_key = 'fDy2oV4J0d1lZaHHVGaBMJrdZisptaAUNaSm4cF9Gc9D7GWTGiD20dAYMJwlUEs6keAZgoZpBLQpzYNo5KVTYg%3D%3D'
access_key2 = 'fDy2oV4J0d1lZaHHVGaBMJrdZisptaAUNaSm4cF9Gc9D7GWTGiD20dAYMJwlUEs6keAZgoZpBLQpzYNo5KVTYg%3D%3D'

json_bus_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
bus_info = []


# 정류소 ID 가져오기

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
           return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print(" [%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def get_Bus_URL(nodeNm) :
    end_point = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getSttnNoList'

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&cityCode=" +str(22)
    parameters += '&nodeNm='+urllib.parse.quote_plus(nodeNm)

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)


def Make_ID_Json(nodeNm):
    jsonData = get_Bus_URL(nodeNm)
    if (jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.') :
        for prn_data in jsonData['response']['body']['items']['item'] :
            json_bus_result.append({'nodeid': prn_data['nodeid'], 'nodenm': prn_data['nodenm']})




# 정류소 도착정보 가져오기

def get_BusInfo_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
           return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print(" [%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def get_BusInfo_URL(nodeID) :
    end_point = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList'

    parameters = "?serviceKey=" + access_key2
    parameters += "&cityCode=" +str(22)
    parameters += '&nodeId='+nodeID

    url = end_point + parameters
    retData = get_BusInfo_Request_URL(url)
    if (retData == None):
        return None
    else:
        return retData


def Make_BusInfo_Xml(nodeID):
    xmlData = get_BusInfo_URL(nodeID)
    tree = ET.ElementTree(ET.fromstring(xmlData))
    root = tree.getroot()
    for bus_ in root.iter('item'):
        bus_info.append(bus_.findtext('routeno'))
        bus_info.append(bus_.findtext('arrprevstationcnt'))
        bus_info.append(bus_.findtext('arrtime'))
        bus_info.append(bus_.findtext('vehicletp'))

    f = open('bus_arrive_info.csv', 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['버스 이름', '도착 전 정거장', '도착 예정 시간(초)', '버스 타입'])

    print('\n<< 버스 도착 정보 >>')
    for x in range(len(bus_info)):
        if x % 4 == 0:
            print('%s 번 버스가' % bus_info[x], end=' ')
        elif x % 4 == 1:
            if int(bus_info[x]) == 1:
                print('전 정류장을 출발하였습니다.', end=' ')
            else:
                print('도착 %s 정거장 전입니다.' % bus_info[x], end='    ')
        elif x % 4 == 2:
            if (int(bus_info[x]) / 60) >= 1:
                print('도착 예정시간: %s분' % (int(bus_info[x]) // 60), end=',    ')
            elif (int(bus_info[x]) / 60) < 1:
                print('도착 예정시간: %s초' % int(bus_info[x]), end=',    ')
        elif x % 4 == 3:
            print('버스 타입 : %s' % bus_info[x])

    y = 0
    for x in range(len(bus_info) // 4):
        csv_writer.writerow([bus_info[y], bus_info[y+1], bus_info[y+2], bus_info[y+3]])
        y+=4

    print('\n"bus_arrive_info"에 버스 도착 정보를 csv 형태로 저장하였습니다.')


def bus_main():
    nodeNm = input('확인할 버스 정류장을 입력하세요 : ')
    Make_ID_Json(nodeNm)

    index = 0
    print('\n<<< 확인할 정류장을 선택하세요 >>>')
    for i in json_bus_result:
        print(str(index+1)+'.', i['nodenm'])
        index += 1
    select_bus = int(input('번호 선택 : '))
    nodeID = ''
    index = 1
    for i in json_bus_result:
        if select_bus == index:
            nodeID = i['nodeid']
            index += 1
        else: index += 1
    Make_BusInfo_Xml(nodeID)

if __name__ == '__main__':
    bus_main()
