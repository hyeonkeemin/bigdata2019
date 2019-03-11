import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1] # 실행인자 : supplier_data.csv

# Create an in-memory SQLite3 database
# Create a table called Supplier with five attributes

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS Suppliers
(Supplier_Name VARCHAR(20),
Invoice_Number VARCHAR(20),
Part_Number VARCHAR(20),
Cost FLOAT,
Purchase_Date DATE);'''

c.execute(create_table)
con.commit()

# Read the CSV file
# Insert the data into the Supplier table

file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader, None) # header 건너뛰고 date만 접근하기 위해서
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()

# Query the Supplier table
output = c.execute('SELECT * FROM Suppliers') # 열 필터링 하는 조건
rows = output.fetchall()
for row in rows:
    output=[]
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
