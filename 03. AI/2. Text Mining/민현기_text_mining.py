# 사용 모델 : 싸이키 런(sklearn) - LogisticRegression
# 독립변수 항목 : 형태소에소 추출된 vocabulary, 단어 빈도

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import re

talk_pattern = re.compile('"(.*?)"')
nottalk_pattern = re.compile('!?["].*?["]')

with open("Harry Potter 1 - Sorcerer's Stone.txt", 'r', encoding='utf-8') as file_handle:
    text = file_handle.read()
    talk = talk_pattern.findall(text)




# vectorizer = CountVectorizer() # 단어 횟수 피처를 만드는 클래스
# term_counts = vectorizer.fit_transform(talk) # 문서에서 단어 횟수를 센다.
# vocabulary = vectorizer.get_feature_names()
#
# # 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# # 단어 빈도(term frequency)가 생성
#
# tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
# features = tf_transformer.transform(term_counts)
#
# # 처리된 파일 저장. 앞으로의 예제에서 사용될 예정
# with open('processed.pickle', 'wb') as file_handle:
#     pickle.dump((vocabulary, features, labels,), file_handle)