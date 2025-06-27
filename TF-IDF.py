from math import log10
from collections import defaultdict

doc1 = "My dog is on my table .".lower().split()
doc2 = "The dog is on the table .".lower().split()
docs = [doc1, doc2]

target_word = "my"

term_count = doc1.count(target_word)
tf = term_count / len(doc1)

doc_count = sum(1 for doc in docs if target_word in doc)
idf = log10(len(docs) / doc_count)

tf_idf = tf * idf
tf_idf_rounded = round(tf_idf, 1)

print(tf_idf_rounded)
