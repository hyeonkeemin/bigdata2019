import pandas
import sys
import MySQLdb

con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='a', passwd='1111',charset='utf8mb4')
c = con.cursor()

input_file = sys.argv[1] # Student_Info_DB_Scheme.xlsx

data_frame = pandas.read_excel('Student_Info_DB_Scheme.xlsx')

data=[]
for row_index in range(len(data_frame)):
    data.append(list(data_frame.loc[row_index]))

for i in range(len(data)):
    print(data[i])
    c.execute('INSERT INTO Students VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");'%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7]))
con.commit()



