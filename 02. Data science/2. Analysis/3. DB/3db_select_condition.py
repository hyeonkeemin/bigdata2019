import sqlite3 # 파이썬에서 제공하는 무료 db
import csv
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
# 전체 레코드 조회
# 열 필터링 조건
# output = c.execute('SELECT Supplier_name,Cost FROM Suppliers')

# 행 필터링 조건
output = c.execute('SELECT * FROM Suppliers WHERE supplier_name="Supplier X" ')

rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
