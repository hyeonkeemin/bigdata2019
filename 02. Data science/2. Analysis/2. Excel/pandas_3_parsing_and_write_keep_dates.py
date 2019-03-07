# 목적 : 날짜 형식 할당
# 근데 판다스로 날짜형식 할당할경우 시분초가 다나옴, 그래서 지우는 직업 별도로 핖요
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

