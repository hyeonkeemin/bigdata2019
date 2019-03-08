import pandas as pd
import numpy

data_frame = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv')

while True:
    menu = int(input('\n메뉴를 선택하세요.\n0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.분산 9.표준편차 10.오름차순 정렬 11.내림차순 정렬\n메뉴 입력 : '))
    if menu == 0:
        break
    else:
        key = input('찾을 데이터를 입력하세요 : ')
        if menu == 1:
            data = data_frame.ix[[int(key)],:]
            print(data)
        elif menu == 2:
            data = data_frame.loc[:, [key]]
            print(data)
        elif menu == 3:
            data = list(data_frame.loc[:, [key]].sum())
            print(data)
        elif menu == 4:
            data = data_frame[[key]]
            print(data.mean)
        elif menu == 5:
            data = data_frame[[key]]
            print(data.max())
        elif menu == 6:
            data = data_frame[[key]]
            print(data.min())
        elif menu == 7:
            pass
        elif menu == 8:
            data = data_frame[[key]]
            print(data.var())
        elif menu == 9:
            data = data_frame[[key]]
            print(data.std())
        elif menu == 10:
            pass
        elif menu == 11:
            pass