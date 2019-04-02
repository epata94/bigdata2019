import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

akco009 = pd.read_csv("niaaa-report2009.csv",index_col="state")
columns = ["wine", "Beer"]
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009["Clusters"] = kmeans.lables

alco2009.to_csv("clustering_Result.csv", lndex=False)

data = alco2009["wine", "Beer"]
label = alco2009["clusters"]

predicted result = kmeans.predict(data)
print("예측 클러스터링 결과")
print(predicted_result)

print("정답률: %s %%"%(metrics.accuracy_score(label,predicted_result)*100))
