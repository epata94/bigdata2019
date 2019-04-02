from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

bmi_read = pd.read_csv("bmi.csv")

label = bmi_read["label"]
height = bmi_read["height"] / 200
weight = bmi_read["weight"] / 80
h_w_concat = pd.concat([weight,height], axis=1)

data_train, data_test, label_train, label_test = train_test_split(h_w_concat, label)

clf = svm.SVC(gamma='auto')
clf.fit(data_train, label_train)

predict_result = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict_result)
cl_report = metrics.classification_report(label_test, predict_result)

print("정답률 =", ac_score)
print("리포트 =\n", cl_report)
