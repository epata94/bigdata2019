import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

nia = pd.read_csv('niaaa-report2009.csv', index_col='State')
columns = ['Beer', 'Wine']

k_means = sklearn.cluster.KMeans(n_clusters=7)
k_means.fit(nia[columns])
nia['Clusters'] = k_means.labels_

nia.to_csv('Clustering_Result.csv', index=False)

data = nia[['Beer', 'Wine']]
label = nia['Clusters']

predict = k_means.predict(data)
print('예측결과\n%s' %predict)

print('\n정답률: %s%%' %(metrics.accuracy_score(label, predict)*100))