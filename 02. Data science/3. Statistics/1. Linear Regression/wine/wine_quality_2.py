import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Read teh data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine_columns = wine.columns.str.replace(' ', '_')

# Display descriptive statistics for quality by wine type
print('와인 종류에 따른 기술통계량 출력')
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantile
print('\n특정 사분위수 계산하기')
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print('\n그룹화, 히스토그램, t 검정')
red_wine = wine.loc[wine['type']=='red', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']

sns.set_style('dark')
print(sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red Wine'))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='White wine'))
plt.xlabel('Quality Score')
plt.ylabel('Density')
plt.title('Distribution of Quality by Wine Type')
plt.legend()
plt.show()

print('\n와인의 종류에 따라 품질의 차이 검정')
print(wine.groupby(['type'])[['quality']].agg(['std','mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat : %.3f pvalue: %.4f'%(tstat,pvalue))