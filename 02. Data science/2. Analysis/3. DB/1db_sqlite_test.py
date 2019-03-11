import sqlite3 # 파이썬에서 제공하는 무료 db

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes

#   // CREATE TABLE : 테이블 생성 명령어
con = sqlite3.connect(':memory:') # 전 파일에 memory에 db 생성을 해놔서 조회가 되야함 but 프로그램이 종료가 되면 날라가는 휘발성이라 조회 ㄴ

# Query the sales table
cursor = con.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Count the number of rows in the output
row_count = 0
for row in rows:
    print(row)
    row_count += 1
print('Number of rows : {}'. format(row_count))

