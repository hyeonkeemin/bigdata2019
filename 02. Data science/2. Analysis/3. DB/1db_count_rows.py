import sqlite3 # 파이썬에서 제공하는 무료 db

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes

#   // CREATE TABLE : 테이블 생성 명령어
con = sqlite3.connect(':memory:')
query = '''CREATE TABLE sales
(customer VARCHAR(20),
product VARCHAR(40),
amount FLOAT,
date DATE);'''

con.execute(query)
con.commit()
# 그러나 휘발성

# Insert a fow rows of data into the table
# ( ) -> db에선 레코드라고 함. 튜플 ㄴㄴ
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
statement = 'INSERT INTO sales VALUES(?, ?, ?, ?)' # sales table에 값을 넣을 것이다
con.executemany(statement, data) # readlines와 비슷함
con.commit()

# Query the sales table
cursor = con.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))