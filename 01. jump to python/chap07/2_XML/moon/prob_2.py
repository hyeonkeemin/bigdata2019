from xml.etree.ElementTree import parse, Element, SubElement, dump

tree = parse('sample.xml')
root = tree.getroot()

profile = []
man=0;woman=0
major_major=0
age_20=0;age_30=0;age_40=0
name_age_20=[];name_age_30=[];name_age_40=[]
lang_name_python=0;lang_experience=0;lang_level_high=0

for i in root.findall('student'):
    name = i.get('name')
    sex = i.get('sex')
    age = int(i.findtext('age'))
    major = i.findtext('major')
    ID = i.get('ID')
    lang=[]
    profile_add = list((name,sex,age,major,lang,ID))
    profile.append(profile_add)
    for x in i.iter('practicable_computer_languages'):
        for y in x:
            lang_name = y.get('name')
            lang_level = y.get('level')
            if lang_level == '상':
                lang_level_high += 1
            if lang_name == '파이썬':
                lang_name_python += 1
            for z in y:
                lang_period = z.get('value')
                lang.append(list((lang_name,lang_level,lang_period)))
    if sex == '남':
        man += 1
    elif sex == '여':
        woman += 1
    if major == '컴퓨터 공학' or major == '통계빅데이터':
        major_major += 1
    if lang:
        lang_experience += 1
    if age < 30 :
        age_20 += 1; name_age_20.append('%s:%s'%(name,age))
    elif 30 <= age < 40:
        age_30 += 1; name_age_30.append('%s:%s'%(name,age))
    else:
        age_40 += 1; name_age_40.append('%s:%s'%(name,age))

def student_system():
    while True:
        input_menu=input('''
        학생정보 XML 데이터 분석 시작..
        
        [메인 메뉴]
        1. 요약 정보
        2. 입력
        3. 조회
        4. 수정
        5. 삭제
        6. 종료
        메뉴 입력 : ''')
        if input_menu == '1':
            print('')
            print('<요약정보>')
            print('* 전체 학생수 : %s명'%len(profile))
            print('* 성별')
            print(' - 남학생 : %s명 (%s%%)'%(man,(man/len(profile))*100))
            print(' - 여학생 : %s명 (%s%%)'%(woman,(woman/len(profile))*100))
            print('* 전공여부')
            print(' - 전공자 : %s명 (%s%%)'%(major_major, (major_major/len(profile))*100))
            print(' - 프로그래밍 언어 경험자 : %s명 (%s%%)'%(lang_experience, (lang_experience/len(profile))*100))
            print(' - 프로그래밍 언어 상급자 : %s명'%lang_level_high)
            print(' - 파이썬 경험자 : %s명'%lang_name_python)
            print('* 연령대')
            print(' - 20대 : %s명 (%s%%) [%s]'%(age_20,(age_20/len(profile))*100,'  '.join(name_age_20)))
            print(' - 30대 : %s명 (%s%%) [%s]'%(age_30,(age_30/len(profile))*100,'  '.join(name_age_30)))
            print(' - 40대 : %s명 (%s%%) [%s]'%(age_40,(age_40/len(profile))*100,'  '.join(name_age_40)))

        elif input_menu == '2':
            print('<신규 학생 정보 입력>')
            while True:
                new_name = input(' - 이름을 입력하세요 (종료는 "Enter" 입력) : ')
                if new_name == '':
                    break
                else:
                    new_sex = input(' - 성별을 입력하세요 : ')
                    new_age = input(' - 나이를 입력하세요 : ')
                    new_major = input(' - 전공을 입력하세요 : ')
                    print(' - 사용가능한 언어를 입력하세요.')
                    student = Element('student', ID='ITT%s'%str(len(root)+1).rjust(3,'0') ,name=new_name, sex=new_sex)
                    SubElement(student, 'age').text = new_age
                    SubElement(student, 'major').text = new_major
                    prac = SubElement(student, 'practicable_computer_languages')
                    while True:
                        new_lang_name = input('  > 언어 이름 (종료는 "Enter" 입력) : ')
                        if new_lang_name =='':
                            break
                        else:
                            new_lang_period = input('  > 학습 기간(년/개월 단위) : ')
                            new_lang_level = input('  > 수준(상/중/하) : ')
                            lang = SubElement(prac, 'language', name=new_lang_name, level=new_lang_level)
                            peri = SubElement(lang, 'period', value=new_lang_period)

                from xml.etree.ElementTree import ElementTree
                root.append(student)
                ElementTree(root).write('sample.xml')


        elif input_menu == '3' :
            while True:
                read_input_menu = input('''
    <조회 서브 메뉴>
    1. 개별 학생 조회
    2. 전체 학생 조회
    3. 상위 메뉴
    메뉴 입력 : ''')
                if read_input_menu == '1':
                    read_condition = input('''
    <검색조건>
    1. ID
    2. 이름
    3. 나이
    4. 전공
    5. 컴퓨터 언어 명
    6. 컴퓨터 언어 학습 기간
    7. 컴퓨터 언어 레벨
    8. 상위 메뉴
    메뉴 입력 : ''')

                    input_search = input('검색어를 입력하세요 : ')
                    if read_condition == '1':
                        for a in root.iter('student'):
                            idc = a.get('ID')
                            if idc == input_search:
                                print('%s (%s)' % (a.get('name'), a.get('ID')))
                                print(' - 성별 : %s' % a.get('sex'))
                                print(' - 나이 : %s' % a.findtext('age'))
                                print(' - 전공 : %s' % a.findtext('major'))
                                for b in a.iter('practicable_computer_languages'):
                                    if not b:
                                        print(' - 사용 가능한 언어 : 없음')
                                    else:
                                        print(' - 사용 가능한 언어')
                                        for c in b:
                                            for d in c:
                                                print('  > %s (학습기간: %s, Level: %s)' % (c.get('name'), d.get('value'), c.get('level')))
                    elif read_condition == '2':
                        for a in root.iter('student'):
                            idc = a.get('name')


                if read_input_menu == '2':
                    pass
                if read_input_menu == '3':
                    continue






        elif input_menu == '4' :
            pass
        elif input_menu == '5' :
            pass
        elif input_menu == '6' :
            break

















        # elif input_menu == '2':
        #     print('')
        #     print('<전체 학생 데이터>')
        #     for student_list in profile:
        #         print('%s'%student_list[0])
        #         print(' - 성별 : %s'%student_list[1])
        #         print(' - 나이 : %s'%student_list[2])
        #         print(' - 전공 : %s'%student_list[3])
        #         if not student_list[4]:
        #             print(' - 사용가능한 컴퓨터 언어 : 없음')
        #         if student_list[4]:
        #             print(' - 사용가능한 컴퓨터 언어')
        #             for lang_list in student_list[4]:
        #                 print('  > %s (학습기간:%s, Level:%s)'%(lang_list[0],lang_list[2],lang_list[1]))
        # elif input_menu == '3':
        #     print('')
        #     print('학생 정보 분석 완료!')
        #     break

def read_check_func():

    return

student_system()
# print(profile)