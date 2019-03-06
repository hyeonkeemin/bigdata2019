# 쓰레기 값 섞였을 때
# 쓰레기 값이 추후 변경될 것이 예상된다면 좀 더 정교한 조건(정규식과 패턴) 활용해야함

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
                row_counter += 1