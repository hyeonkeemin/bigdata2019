import pandas as pd
from sklearn import svm, metrics

house = pd.read_csv('Housing.csv')
house_col = house.columns.str.replace(' ', '_')

dependent_variable = house.loc[:, 'price']
independent_variable = house[house.columns.difference([''])]