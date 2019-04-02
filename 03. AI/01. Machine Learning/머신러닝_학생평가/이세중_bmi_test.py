from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

bmi_data = pd.read_csv("bmi.csv")
data= bmi_data[['height','weight']]
label = bmi_data['label']
train_data, pre_data, train_label,pre_label = train_test_split(data,label)
clf = svm.SVC()
clf.fit(train_data, train_label)
predict = clf.predict(pre_data)
print("정확도 :"+str(metrics.accuracy_score(pre_label, predict)*100)+"%")
print("리포트 :"+str(metrics.classification_report(pre_label, predict)))