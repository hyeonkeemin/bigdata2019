import json
with open('ITT_Student.json',encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_data = json.loads(json_string)


while True:
    menu = input('''\n\n<<<< JSON기반 학생 정보 관리 프로그램 >>>>\n\n1. 학생 정보 입력\n2. 학생 정보 조회\n3. 학생 정보 수정\n4. 학생 정보 삭제\n5. 프로그램 종료\n메뉴를 선택하세요 : ''')
    if menu == '1':
        newinput_name = input('이름 : ')
        newinput_age = int(input('나이 : '))
        newinput_address = input('주소 : ')
        newinput_pastexperience = int(input('과거 수강 횟수 : '))
        newinput_presentlecture = input('현재 수강 과목이 있습니까?( y/n 으로 입력) : ')
        newinput_code = input('강의 코드 : ')
        newinput_lecturename = input('강의 명 : ')
        newinput_teacher = input('강사 이름 : ')
        newinput_openlecturedate = input('개강일(yyyy-mm-dd) : ')
        newinput_closelecturedate = input('종료일(yyyy-mm-dd) : ')
        newinput_morepresentlecture = input('현재 수강하는 과목이 더 있습니까? ( y/n 으로 입력) : ')

        json_data.append({})
        json_data[len(json_data)-1].update({'address':newinput_address})
        json_data[len(json_data)-1].update({'student_ID':('ITT%s'%str(len(json_data)).rjust(3,'0'))})
        json_data[len(json_data)-1].update({'student_age':newinput_age})
        json_data[len(json_data)-1].update({'student_name':newinput_name})
        json_data[len(json_data)-1].update({'total_course_info':{}})
        json_data[len(json_data)-1]['total_course_info'].update({'learning_course_info':[]})
        json_data[len(json_data) - 1]['total_course_info']['learning_course_info'].append({'close_date': newinput_closelecturedate, 'course_code': newinput_code, 'course_name': newinput_lecturename,'open_date': newinput_openlecturedate, 'teacher': newinput_teacher})

        if newinput_morepresentlecture == 'y':
            while True:
                newinput_code_y = input('강의 코드(종료는 "Enter" 입력) : ')
                if newinput_code_y == '':break
                else:
                    newinput_lecturename_y = input('강의 명 : ')
                    newinput_teacher_y = input('강사 이름 : ')
                    newinput_openlecturedate_y = input('개강일(yyyy-mm-dd) : ')
                    newinput_closelecturedate_y = input('종료일(yyyy-mm-dd) : ')
                    json_data[len(json_data)-1]['total_course_info']['learning_course_info'].append({'close_date':newinput_closelecturedate_y,'course_code':newinput_code_y,'course_name':newinput_lecturename_y,'open_date':newinput_openlecturedate_y,'teacher':newinput_teacher_y})

        json_data[len(json_data) - 1]['total_course_info'].update({'num_of_course_learned': newinput_pastexperience})

    elif menu == '2':
        read_menu = input('''\n아래 메뉴를 선택하세요\n1. 전체 학생정보 조회\n  검색 조건 선택\n2. ID 검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강 중인 학생\n8. 현재 수강 중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n 메뉴를 선택하세요 : ''')
        if read_menu == '1':
            for full_list in json_data:
                print('\n* 학생 ID : %s' % full_list['student_ID'])
                print('* 이름 : %s' % full_list['student_name'])
                print('* 나이 : %s' % full_list['student_age'])
                print('* 주소 : %s' % full_list['address'])
                print('* 수강 정보')
                print('  + 과거 수강 횟수 : %s' % full_list['total_course_info']['num_of_course_learned'])
                print('  + 현재 수강 과목')
                for lesson_list in full_list['total_course_info']['learning_course_info']:
                    print('     강의 코드 : %s' % lesson_list['course_code'])
                    print('     강의명 : %s' % lesson_list['course_name'])
                    print('     강사 : %s ' % lesson_list['teacher'])
                    print('     개강일 : %s' % lesson_list['open_date'])
                    print('     종료일 : %s\n' % lesson_list['close_date'])
        else:
            if read_menu=='10':
                continue
            else:
                ok_list=[]
                input_search=input('검색어를 입력하세요 : ')
                if read_menu == '2':
                    for full_list in json_data:
                        if input_search in full_list['student_ID']:
                            ok_list.append(full_list)
                elif read_menu == '3':
                    for full_list in json_data:
                        if input_search in full_list['student_name']:
                            ok_list.append(full_list)
                elif read_menu == '4':
                    for full_list in json_data:
                        if int(input_search) == full_list['student_age']:
                            ok_list.append(full_list)
                elif read_menu == '5':
                    for full_list in json_data:
                        if input_search in full_list['address']:
                            ok_list.append(full_list)
                elif read_menu == '6':
                    for full_list in json_data:
                        if int(input_search) == full_list['total_course_info']['num_of_course_learned']:
                            ok_list.append(full_list)
                elif read_menu == '7':
                    for full_list in json_data:
                        for lesson_list in full_list['total_course_info']['learning_course_info']:
                            if input_search in lesson_list['course_code']:
                                ok_list.append(full_list)
                elif read_menu == '8':
                    for full_list in json_data:
                        for lesson_list in full_list['total_course_info']['learning_course_info']:
                            if input_search in lesson_list['course_name']:
                                ok_list.append(full_list)
                elif read_menu == '9':
                    for full_list in json_data:
                        for lesson_list in full_list['total_course_info']['learning_course_info']:
                            if input_search in lesson_list['teacher']:
                                ok_list.append(full_list)

            if len(ok_list) == 1:
                for i in ok_list:
                    print('\n* 학생 ID : %s' % i['student_ID'])
                    print('* 이름 : %s' % i['student_name'])
                    print('* 나이 : %s' % i['student_age'])
                    print('* 주소 : %s' % i['address'])
                    print('* 수강 정보')
                    print('  + 과거 수강 횟수 : %s' % i['total_course_info']['num_of_course_learned'])
                    print('  + 현재 수강 과목')
                    for lesson_list in i['total_course_info']['learning_course_info']:
                        print('     강의 코드 : %s' % lesson_list['course_code'])
                        print('     강의명 : %s' % lesson_list['course_name'])
                        print('     강사 : %s ' % lesson_list['teacher'])
                        print('     개강일 : %s' % lesson_list['open_date'])
                        print('     종료일 : %s\n' % lesson_list['close_date'])
            elif len(ok_list) >= 2:
                print('\n복수 개의 결과가 검색되었습니다.')
                for i in ok_list:
                    print('>> 학생 ID : %s, 학생 이름: %s' % (i['student_ID'], i['student_name']))

    elif menu == '3':
        search_id = input('\n수정할 학생의 ID를 입력하세요 : ')
        while True:
            for search_list in json_data:
                if search_id == search_list['student_ID']:
                    input_update_menu = input('''1. 학생 이름\n2: 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴\n메뉴 번호를 입력하세요 : ''')
                    if input_update_menu == '0':break
                    elif input_update_menu == '1':pass
                    elif input_update_menu == '2':pass
                    elif input_update_menu == '3':pass
                    elif input_update_menu == '4':pass
                    elif input_update_menu == '5':
                        index = 1
                        print('\n<현재 수강중인 강의 정보>')
                        for presnt_lecture in search_list['total_course_info']['learning_course_info']:
                            print(str(index)+'.','강의 코드 : %s' % presnt_lecture['course_code'])
                            print(str(index+1)+'.', '강의명 : %s' % presnt_lecture['course_name'])
                            print(str(index+2)+'.', '강사 : %s' % presnt_lecture['teacher'])
                            print(str(index+3)+'.', '개강일 : %s' % presnt_lecture['open_date'])
                            print(str(index+4)+'.', '종료일 : %s\n' % presnt_lecture['close_date'])
                            index += 5
                        want_update_menu = input('변경을 원하는 메뉴를 선택하세요 : ')
                        for presnt_lecture in search_list['total_course_info']['learning_course_info']:
                            pass




    elif menu == '4':
        pass

    elif menu == '5':
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('ITT_Student.json SAVED')
            break




