import threading
import time
import ctypes

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

def update_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(3)
            print('발코니 상태 변경')
            g_Balcony_Windows = not g_Balcony_Windows

while True:
    print("\n메뉴를 선택하세요")
    print("1. 장비 선택 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num = int(input("메뉴 입력: "))
    if(menu_num==1):
        print("\n발코니(베란다) 창문: ", end=' ')
        if g_Balcony_Windows==True: print("열림")
        else:print("닫힘")
    elif(menu_num==2):
        print("\n인공지능 모드: ", end=' ')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode == True:
            print("인공지능 모드 작동")
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("인공지능 모드 정지")
    else: break