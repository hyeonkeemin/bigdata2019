import pandas as pd
from statsmodels.formula.api import ols, glm
from itertools import combinations
import operator

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)

wine.columns = wine.columns.str.replace(' ', '_')
formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(formula, data=wine).fit()


# 모형 요약
print(lm.summary())


# 예측
quality = list(wine.loc[ :, 'quality'])
my_combination = 'quality ~ '
independent_col_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
my_dict = {}
for i in range(1, len(independent_col_list)+1):
    comb = list(combinations(independent_col_list, i))
    for comb_tup in comb:
        comb_data = ' + '.join(list(comb_tup))
        my_formula = my_combination + comb_data
        my_lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables = wine[wine.columns.difference(['quality', 'type'])]
        new_observations = wine.loc[wine.index.isin(range(len(wine))), independent_variables.columns]

        y_predicted = my_lm.predict(new_observations)
        y_predicted_rounded = [round(score) for score in y_predicted]

        ok = 0
        for num in range(len(wine)):
            if y_predicted_rounded[num] == quality[num]:
                ok += 1
        # print('변수 : %s' % my_formula)
        # print('정답률 : %s' % round(ok/len(wine)*100, 2))
        my_dict['%s'%my_formula] = round(ok/len(wine)*100, 2)

my_dict = sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True)
print('\n정답률이 최대가 되는 조합: %s \n정답률: %s' %(my_dict[0][0], my_dict[0][1]))