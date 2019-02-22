import json #json을 쓰기 위한 모듈

g = json_big_data=[]

with open('sample.json',encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    g_json_big_data = json.loads(json_string)

#json 값 가져오기
print(g_json_big_data)
print(g_json_big_data[0])

#json 데이터 읽기(read)
print(g_json_big_data[0]['레벨 2-1 키'])

#json 데이터 쓰기, 삽입(create)
g_json_big_data.append({'레벨 2-4 키':'수박'})
pass #디버그로 확인용 pass

#json 데이터 수정(update)
g_json_big_data[0]['레벨 2-1 키'] = '체리'
pass

#json 데이터 삭제(delete)
del g_json_big_data[2]
pass

#자식 레벨의 딕셔너리 접근
print(g_json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['레벨 4-1 키'])
#자식 레벨의 딕셔너리 수정
g_json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['레벨 4-1 키']=24 #json은 타입이 정수형인지, 문자형인지, 딕셔너린지, 리스튼지 확인 잘해야된다잉
pass

with open('sample_modify_json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
    print('ITT_Student.json SAVED')
