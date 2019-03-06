# 쓰레기 값 섞였을 때
# 쓰레기 값이 추후 변경될 것이 예상된다면 좀 더 정교한 조건(정규식과 패턴) 활용해야함

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)
