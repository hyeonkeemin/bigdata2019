# pandas를 이용한 파일 읽고 쓰기

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False) # index: for문 돌리면서 행에 1씩 증가시키는거랑 똑같은 기능