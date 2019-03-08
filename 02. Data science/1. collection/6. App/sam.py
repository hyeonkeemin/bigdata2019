import json

with open('동구_신암동_초단기예보조회.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_weather_data = json.loads(json_string)

data = []
index = 0
print(len(json_weather_data))

for i in json_weather_data:
    index += 1
    if index % 4 == 2:
        data.append(i)
