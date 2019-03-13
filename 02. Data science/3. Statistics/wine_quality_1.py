import pandas as pd

# Read the data set into a pandas DataFrame

wine = pd.read_csv('winequality-both.csv', sep=',', header=0) # 헤더행=0행
wine.columns = wine.columns.str.replace(' ', '_') # 중요함

print(wine.head())
print(wine.head(10))

print('변수별 요약통계 표시')
print(wine.describe())

print('\n유일값 찾기')
print(sorted(wine.quality.unique())) # 데이터 유형 찾는데 적합

print('\n빈도 찾기')
print(wine.quality.value_counts()) # 높은거 내림차순