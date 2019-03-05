import threading
import ctypes
import time
from Weather_Realtime_info_for_student import *

g_Balcony_Windows = False
g_AI_Mode = False

def terminate_ai_mode():
    """Terminates a python thread from another thread.
    :param thread:athreading.Thread instance
    """
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def update_weather_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(10)
            get_Realtime_Weather_Info()
            with open('동구_신암동_초단기예보조회.json', encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                json_weather_data = json.loads(json_string)

            data = []
            index = 0
            for i in json_weather_data:
                index += 1
                if index % 4 == 1:
                    data.append(i)

            slicing = data[0]
            print('%s년 %s월 %s일 %s시 %s분 기상정보' % (
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
                        pass
                    elif i['fcstValue'] == 1:
                        print('비가 내리겠습니다.')
                    elif i['fcstValue'] == 2:
                        print('눈과 비가 섞여서 내리겠습니다.')
                    elif i['fcstValue'] == 3:
                        print('눈이 내리겠습니다.')

            if g_Balcony_Windows == False:
                select = input('창문을 여시겠습니까?(y/n)')
                if select == 'y':
                    print('창문을 열겠습니다.')
                    g_Balcony_Windows = not g_Balcony_Windows
                elif select == 'n':
                    print('창문 닫아놓겠습니다.')
            elif g_Balcony_Windows == True:
                select = input('창문을 닫으시겠습니까?(y/n) : ')
                if select == 'y':
                    print('창문을 닫겠습니다.')
                    g_Balcony_Windows = not g_Balcony_Windows
                elif select == 'n':
                    print('창문 열어놓겠습니다.')

while True:
    g_AI_Mode = not g_AI_Mode
    if g_AI_Mode == True:
        print("인공지능 모드가 작동 되었습니다. 30분마다 자동으로 날씨 정보를 얻고 창문을 열고 닫을 수 있습니다.")
        ai_scheduler = threading.Thread(target=update_weather_scheduler())
        ai_scheduler.daemon = True
        ai_scheduler.start()
    else:
        while ai_scheduler.is_alive():
            try:
                terminate_ai_mode()
            except:
                pass
        print("인공지능 모드 정지")
