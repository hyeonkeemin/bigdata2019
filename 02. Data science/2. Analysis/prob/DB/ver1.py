import pandas
import MySQLdb

def summary_info():
    print('\n1ㄱㄷㄱㄷ')

def read():
    read_menu = int(input('\n<< 조회 서브 메뉴>>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위메뉴\n메뉴 입력 : '))


def sql_menu():
    while True:
        menu = int(input(
            '\n<<< MySQL 기반 학생정보 데이터 분석 시작.. >>>\n\n[메인메뉴]\n1. 요약정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료\n메뉴 입력 : '))
        if menu == 1:
            summary_info()
        elif menu == 2:
            pass
        elif menu == 3:
            read()
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            break

def sql_main():
    con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='a', passwd='1111',charset='utf8mb4')
    c = con.cursor()

    data_frame = pandas.read_excel('Student_Info_DB_Scheme.xlsx')

    data=[]
    for row_index in range(len(data_frame)):
        data.append(list(data_frame.loc[row_index]))

    for i in range(len(data)):
        c.execute('INSERT INTO Students VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");'%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7]))
    con.commit()
    sql_menu()

if __name__ == '__main__':
    sql_main()
