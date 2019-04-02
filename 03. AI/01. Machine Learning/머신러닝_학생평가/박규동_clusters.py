import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

alco_2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco_columns = ["Beer", "Wine"]

alco_kmeans = sklearn.cluster.KMeans(n_clusters=9)
alco_kmeans.fit(alco_2009[alco_columns])

alco_2009["Clusters"] = alco_kmeans.labels_
alco_2009.to_csv("Clustering_Result.csv")

data = alco_2009[["Beer", "Wine"]]
label = alco_2009["Clusters"]

predicted_result = alco_kmeans.predict(data)
print("예측결과 = ", predicted_result)
print("정답률 = %s %%" %(metrics.accuracy_score(label,predicted_result)*100))

