import pandas as pd
import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

df_train = pd.read_csv('Train.txt', delimiter='\t', keep_default_na=False) # 결측값은 NaN으료 표시
df_test = pd.read_csv('Test.txt', delimiter='\t', keep_default_na=False)

print(df_train.head())

text_train, y_train = df_train['document'].values, df_train['label'].values
text_test = df_test['document'].values
y_test = df_test['label'].values

