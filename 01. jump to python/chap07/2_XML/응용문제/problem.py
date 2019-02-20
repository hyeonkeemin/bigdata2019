from xml.etree.ElementTree import parse
tree = parse('students_info.xml')
student_list = tree.getroot()

name_tag = student_list.find('name')
print(name_tag)


# while True:
#     input_menu = input('''학생정보 XML 데이터 분석 시작..
#     1. 요약 정보
#     2. 전체 데이터 조회
#     3. 종료
#
#     ''')
#     if input_menu == '1':
#
#         print('''
#         <요약정보>
#         * 전체 학생수 : %s 명
#         * 성별
#             - 남학생 : %s 명(%s%)
#             - 여학생 : %s 명(%s%)
#         * 전공여부
#             - 전공자(컴퓨터 공학, 통계) : %s 명(%s%)
#             - 프로그래밍 언어 경험자 : %s 명(%s%)
#             - 프로그래밍 언어 상급자 : %s 명(%s%)
#             - 파이썬 경험자 : %s 명(%s%)
#         * 연령대
#             - 20대 : %s명(%s%)
#             - 30대 : %s명(%s%)
#             - 40대 : %s명(%s%)
#         ''')
#
#     elif input_menu == '2':
#         pass
#
#     elif input_menu == '3':
#         break

