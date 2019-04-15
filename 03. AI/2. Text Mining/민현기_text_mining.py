import pandas as pd
import konlpy
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV


df_train = pd.read_csv('Train.txt', delimiter='\t', keep_default_na=False) # 결측값은 NaN으료 표시
df_test = pd.read_csv('Test.txt', delimiter='\t', keep_default_na=False)

print(df_train.head())

text_train, y_train = df_train['document'].values, df_train['label'].values
text_test = df_test['document'].values
y_test = df_test['label'].values

okt_tag = Okt()

def okt_tokenizer(text):
    return okt_tag.morphs(text) # morphs : 형태소 추출, nouns : 명사 추출, pos : 품사 부착

okt_param_grid = {'tfidfvectorizer_min_df': [3,5,7],
                  'tfidvectorizer_ngram_ragne' : [(1,1), (1,2), (1,3)],
                  'logisticregression_C': [0.1, 1, 10, 100]}

okt_pipe = make_pipeline(TfidfVectorizer(tokenizer=okt_tokenizer), LogisticRegression(solver='liblinear'))
okt_grid = GridSearchCV(okt_pipe, okt_param_grid, cv=5)


# 그리드 서치 수행
okt_grid.fit(text_train[0:1000], y_train[0:1000])
print('최상의 크로스 밸리데이션 점수: {:.3f}'.format(okt_grid.best_score_))
print('최적의 크로스 밸리데이션 파라미터: ', okt_grid.best_params_)

X_test_okt = okt_grid.best_estimator_.named_stpes['tfidfvectorizer'].transform(text_test)
score = okt_grid.best_estimator_.named_stpes['logisticregression'].score(X_test_okt, y_test)
print('테스트 점수: {:.3f}'.format(score))