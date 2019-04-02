import pandas as pd
from sklearn.cluster import KMeans
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

alcohol = pd.read_csv("niaaa-report2009.csv","w",index_col="State")
data_columns = ["Beer","Wine"]
kmeans = KMeans(n_clusters=9).fit(alcohol[data_columns])
alcohol["Clusters"] = kmeans.labels_

data = alcohol[data_columns]
label = alcohol["Clusters"]

result = kmeans.predict(data)
print("정답률 :"+metrics.accuracy_score(label,result))


