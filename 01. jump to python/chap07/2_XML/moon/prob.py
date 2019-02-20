from xml.etree.ElementTree import parse
tree = parse('students_info.xml')
root = tree.getroot()

profile=[]
name=[]
sex=[]
sex_man=0;sex_woman=0
age=[]
age_20=0;age_30=0;age_40=0
major=[]
major_major=0
lang_name=[]
lang_name_python=0;lang_experience=0
lang_level=[]
lang_level_high=0
lang_period=[]

for element in root.findall('student'):
    name.append(element.get('name'))
    sex.append(element.get('sex'))
    age.append(element.findtext('age'))
    major.append(element.findtext('major'))
    for parent in element.iter('practicable_computer_languages'):
        for child in parent:
            lang_name.append(child.get('name'))
            lang_level.append(child.get('level'))
            for ch_child in child:
                lang_period.append(ch_child.get('value'))


def student():
    input_menu=input('''학생정보 XML 데이터 분석 시작..
    1. 요약 정보
    2. 전체 데이터 조회
    3. 종료

    ''')

    if input_menu == '1':
        print('')
        print('<요약정보>')
        print('* 전체 학생수 : %s명'%len(name))
        print('* 성별')
        print(' - 남학생 : %s명 (%s%%)'%(sex_man,(sex_man/len(sex))))
        print(' - 여학생 : %s명 (%s%%)'%(sex_woman,(sex_woman/len(sex))))
        print('* 전공여부')
        print(' - 전공자 : %s명 (%s%%)'%(major_major, (major_major/len(major))))
        print(' - 프로그래밍 언어 경험자 : %s명 (%s%%)'%(lang_experience, (lang_experience/len(major))))
        print(' - 프로그래밍 언어 상급자 : %s명'%lang_level_high)
        print(' - 파이썬 경험자 : %s명'%lang_name_python)
        print('* 연령대')
        print(' - 20대 : %s명'%age_20)
        print(' - 30대 : %s명'%age_30)
        print(' - 40대 : %s명'%age_40)
    elif input_menu == '2':
        pass
    elif input_menu == '3':
        exit()

student()

