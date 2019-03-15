import pandas as pd
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ','_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates +' \
             'total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

print('< lm.summary()')
print(lm.summary())

print('')
print('Quantities you can extract from the result: %s' % dir(lm))
print('Coefficients: %s' % lm.params)
print('Coefficient Std Error: ' % lm.rsquared_adj)
print('F-statistic: %.1f P-value: %.2f' % (lm.fvalue, lm.f_pvalue))
print('Number of obs: %s / Number of fitted values: %s' % (lm.nobs, len(lm.fittedvalues)))