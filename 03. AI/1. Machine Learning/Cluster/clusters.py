import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt

alco2009 = pd.read_csv('niaaa-report2009.csv', index_col='State')
columns = ['Wine', 'Beer']


# 클러스터링 객체를 생성하고 모델을 학습시킨다.
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009['Clusters'] = kmeans.labels_

# cluster 변수는 사람의 직관에 의해 설정되고 수행된 결과에 따라 재조정함
# 클러스터링 된 결과가 의미가 있다고 판단했을 때 최종 클러스터링 변수 확정

alco2009.to_csv('Clustering_Result.csv', index=False)

data = alco2009[['Wine', 'Beer']]
label = alco2009['Clusters']

predicted_result = kmeans.predict(data)

print('예측 클러스터링 결과')
print(predicted_result)
print('정답률 : %s%%' %(metrics.accuracy_score(label, predicted_result)*100))

