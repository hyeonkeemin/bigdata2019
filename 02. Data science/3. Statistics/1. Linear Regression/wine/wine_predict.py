import pandas as pd
from statsmodels.formula.api import ols, glm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type'])]

new_observations = wine.loc[wine.index.isin(range(len(wine))), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]


