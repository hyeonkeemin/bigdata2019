import pandas as pd
from statsmodels.formula.api import ols, glm
import matplotlib.pyplot as plt
import seaborn as sns

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type'])]

new_observations = wine.loc[wine.index.isin(range(len(wine))), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]

print(y_predicted)
# print(lm.summary())
# print('')

# print('결정계수: %s' % round(lm.rsquared_adj, 5))
# print('F-statistic: %.1f // P-value: %.2f' % (lm.fvalue, lm.f_pvalue))



# 예제
ok = 0
quality = list(wine.loc[ :, 'quality'])
for i in range(len(wine)):
    if y_predicted_rounded[i] == quality[i]:
        ok+=1
print('\n정답률 : %s%%' % (round(ok/len(wine)*100, 2)))