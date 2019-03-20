import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 붓꽃의 CSV 데이터 읽어 들이기
csv = pd.read_csv('iris.csv')

# 필요한 열 추출하기
csv_data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
csv_label = csv['Name']

# 학습 전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

'''
train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)

(1) Parameter
arrays : 분할시킬 데이터를 입력 (Python list, Numpy array, Pandas dataframe 등..)
test_size : 테스트 데이터셋의 비율(float)이나 갯수(int) (default = 0.25)
train_size : 학습 데이터셋의 비율(float)이나 갯수(int) (default = test_size의 나머지)
random_state : 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값 (int나 RandomState로 입력)
shuffle : 셔플여부설정 (default = True)
stratify : 지정한 Data의 비율을 유지한다. 예를 들어, Label Set인 Y가 25%의 0과 75%의 1로 이루어진 Binary Set일 때,
            stratify=Y로 설정하면 나누어진 데이터셋들도 0과 1을 각각 25%, 75%로 유지한 채 분할된다.
'''

# 데이터 학습시키고 예측하기
clf = svm.SVC(gamma='auto')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print('전체 데이터 수: %d' %(len(csv_data)))
print('학습 전용 데이터 수: %d' %(len(train_data)))
print('테스트 데이터 수: %d' %(len(test_data)))
print('정답률: ', ac_score)