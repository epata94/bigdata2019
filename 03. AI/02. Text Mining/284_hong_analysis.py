from gensim.models import word2vec

model  = word2vec.Word2Vec.load("hong.model")

print(model.most_similar(positive=["대통령"]))
# most_similar: 키워드와 유사한 또는 같이 많이 언급된 단어