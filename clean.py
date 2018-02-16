def clean10(corpus):
    word_dict={}
    for abstract in corpus:
        for word in abstract.split():
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1
    top_10=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)[:10]

    cleansed_corpus=[]
    for abstract in corpus:
        #print abstract
        new_abstract=' '.join([word  for word in abstract.split() if word not in top_10])
        #print word_arr
        cleansed_corpus.append(new_abstract)
    return(cleansed_corpus,top_10)