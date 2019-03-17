import pandas as pd
from statsmodels.formula.api import ols, glm
import operator
from itertools import combinations

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)

wine.columns = wine.columns.str.replace(' ', '_')
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

# 모형 요약
# print(lm.summary())

# 예측
ok = 0
quality = list(wine.loc[ :, 'quality'])
my_combination = 'quality ~ '
for i in range(len(wine)):
    comb = list(combinations(wine.columns,i))
    for comb_tup in comb:
        if len(comb_tup) == 0:
            del comb_tup
        else:
            comb_data = ' + '.join(list(comb_tup))
            data = my_combination + comb_data
            lm = ols(data, data=wine).fit()
            dependent_variable = wine['quality']
            independent_variables = wine[wine.columns.difference(['quality', 'type'])]
            new_observations = wine.loc[wine.index.isin(range(len(wine))), independent_variables.columns]
            y_predicted = lm.predict(new_observations)
            y_predicted_rounded = [round(score) for score in y_predicted]
            print(y_predicted)

# print('\n정답률 : %s%%' % (round(ok/len(wine)*100, 2)))

