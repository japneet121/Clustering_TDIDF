from clean import clean10
from cluster import create_cluster
from scrap import  scrapData
from wordVectorizer import getWordVec
from nltk.corpus import stopwords
from cluster import create_cluster
from sklearn.feature_extraction.text import TfidfVectorizer
    
stopWords = set(stopwords.words('english'))

if __name__=="__main__":
    print "Scraping Data ........"
    abstracts=scrapData()
    print "Data Scraped"
    print"Data sent for cleaning.........."
    clean_abstract,words_removed=clean10(abstracts)
    print "Words removed are",words_removed
    tf_matrix=getWordVec(clean_abstract)
    print"Vectors are ready.."
    print "First Vector",tf_matrix.todense()[0]
    print "Second Vector",tf_matrix.todense()[0]




    clean_stop=[]
    for text in clean_abstract:
        text=' '.join([word.lower()  for word in text.split() if word.lower() not in stopWords])
        text=text.decode('unicode_escape').encode('ascii','ignore')
        clean_stop.append(text)
        tf_mat_stop=getWordVec(clean_stop)


    kmeans1_stop=create_cluster(sparse_data=tf_mat_stop,nclust=6)
    trans_mat_stop=kmeans1_stop.transform(tf_mat_stop)

    clust_dict_stop={}
    for i,label in enumerate(kmeans1_stop.labels_):
        if label in clust_dict_stop:
            clust_dict_stop[label].append(clean_stop[i])
        else:
            clust_dict_stop[label]=[]
            clust_dict_stop[label].append(clean_stop[i])
    print "cluster_dict created"

    keywords={}
    for key in clust_dict_stop:
        word_dict={}
        for abstract in clust_dict_stop[key]:
            for word in abstract.split():
                if word in word_dict:
                    word_dict[word]+=1
                else:
                    word_dict[word]=1
        keywords[key]=word_dict
    

    transformer = TfidfVectorizer(encoding='utf-8',max_features=3)

    transformer.fit(clust_dict_stop[0])
    print "Cluster 1",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)
    
    transformer.fit(clust_dict_stop[1])
    print "Cluster 2",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)
    
    transformer.fit(clust_dict_stop[2])
    print "Cluster 3",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)
    
    transformer.fit(clust_dict_stop[3])
    print "Cluster 4",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)
    
    transformer.fit(clust_dict_stop[4])
    print "Cluster 5",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)
    
    transformer.fit(clust_dict_stop[5])
    print "Cluster 6",sorted(transformer.vocabulary_.items(),key=lambda x:x[0],reverse=True)

