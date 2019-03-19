import pandas as pd
from sklearn import svm, metrics

wine = pd.read_csv('winequality-both.csv', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

independent_variable = wine.loc[:,'quality']
dependent_variable = wine[wine.columns.difference(['quality', 'type'])]

clf = svm.SVC(gamma='auto')
clf.fit(dependent_variable, independent_variable)
pre = clf.predict(dependent_variable)

ac_score = metrics.accuracy_score(independent_variable, pre)
print('정답률 : %s%%' % round(ac_score*100, 2))