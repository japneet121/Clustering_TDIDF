# Clustering_TDIDF
Steps followed For this case study

* Investigated the HTTP mechanism for the scrapping URL.
* Parameters for the post request were identified to get 100 search records
* The Abstract for these records were fetched using scrapping framework BeautifulSoup
* A dictionary for the word counted was created  and the top 10 words were removed from the corpus
* The vectors for these abstracts were created using CountVectorizer
* To get the unique words some preprocessing steps were followed
  - Lower case for all words
  - Removal of stop words
  - TFIDF score calculation of words
* After preprocessing step the K Means Algorithm was used with kmean++ initializer to get the 6 clusters from the corpus
* In the algorithm the cosine_similarity metric was used to calculate the distance

# Libraries Used
* BeautifulSoup
* Sklearn
* pandas
# Algotithms Used
* Word Vectorizer
* TF-IDF Vectorization
* K Means
* Kmeans++
