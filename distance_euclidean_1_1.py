import pandas as pd
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

sentence_1 = "My dog is on my table ."
sentence_2 = "The dog is on the table ."

stop_words = ['can', 'is', 'if', "the", 'have', 'that', 'been']

CountVec = CountVectorizer(ngram_range=(1, 1), stop_words=stop_words)
Count_data = CountVec.fit_transform([sentence_1, sentence_2])

cv_dataframe = pd.DataFrame(Count_data.toarray(), columns=CountVec.get_feature_names_out())
print(cv_dataframe)

a = cv_dataframe.loc[0].values
b = cv_dataframe.loc[1].values
dst = distance.euclidean(a, b)
print(dst)
