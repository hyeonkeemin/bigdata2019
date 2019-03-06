import json

with open('동구_신암동_초단기예보조회.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_weather_data = json.loads(json_string)

data = []
index = 0
for i in json_weather_data:
    index += 1
    if index % 4 == 2:
        data.append(i)

slicing = data[0]
print('\n%s년 %s월 %s일 %s시 %s분 기상정보' % (
    str(slicing['fcstDate'])[0:4], str(slicing['fcstDate'])[4:6], str(slicing['fcstDate'])[6:8],
    str(slicing['fcstTime'])[0:2], str(slicing['fcstTime'])[2:4]))

for i in data:
    if i['category'] == 'T1H':
        print('기온은 %s도 입니다.' % i['fcstValue'])
    elif i['category'] == 'SKY':
        if i['fcstValue'] == 1:
            print('하늘은 맑겠습니다.')
        elif i['fcstValue'] == 2:
            print('구름이 조금 끼겠습니다.')
        elif i['fcstValue'] == 3:
            print('구름이 많이 있겠습니다.')
        elif i['fcstValue'] == 4:
            print('날씨는 흐리겠습니다.')
    elif i['category'] == 'REH':
        print('습도는 %s%% 입니다.' % i['fcstValue'])
    elif i['category'] == 'PTY':
        if i['fcstValue'] == 0:
            print('비는 내리지 않겠습니다.')
        elif i['fcstValue'] == 1:
            print('비가 내리겠습니다.')
        elif i['fcstValue'] == 2:
            print('눈과 비가 섞여서 내리겠습니다.')
        elif i['fcstValue'] == 3:
            print('눈이 내리겠습니다.')

for b in data:
    print(b)
