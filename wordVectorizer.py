from sklearn.feature_extraction.text import CountVectorizer

def getWordVec(corpus):
    vectorizer = CountVectorizer(encoding='utf-8')
    tf_mat=vectorizer.fit_transform(corpus)
    return tf_mat