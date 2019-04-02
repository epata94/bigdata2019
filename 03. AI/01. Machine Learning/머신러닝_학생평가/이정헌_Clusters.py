import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics


alco=pd.read_csv("niaaa-report2009.csv",index_col="State")
columns=["Wine","Beer"]
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco[columns])
alco["Clusters"] = kmeans.labels_
alco.to_csv("Clustering_Result.csv",index=False)
data=alco[["Wine","Beer"]]
label=alco["Clusters"]
predicted_result=kmeans.predict(data)
print("예측 클러스트링 결과")
print(predicted_result)
print("정답률: %s %%"%(metrics.accuracy_score(label,predicted_result)*100))

