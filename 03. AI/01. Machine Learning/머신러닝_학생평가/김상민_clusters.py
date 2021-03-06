import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

alcohol_data = pd.read_csv('niaaa-report2009.csv', index_col="State")
columns = ['Wine', 'Beer']

k_means = sklearn.cluster.KMeans(n_clusters=9)
k_means.fit(alcohol_data[columns])

alcohol_data['Clusters'] = k_means.labels_
alcohol_data.to_csv('Clustering_Result.csv', index=False)

data = alcohol_data[columns]
label = alcohol_data['Clusters']


predict_alcohol = k_means.predict(data)

print("==== 예측 결과 ====")
print(predict_alcohol)
print("정답률 : %s %%" % (metrics.accuracy_score(label, predict_alcohol)*100))