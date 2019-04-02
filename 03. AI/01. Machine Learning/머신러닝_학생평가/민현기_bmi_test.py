import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

bmi = pd.read_csv('bmi.csv', header=0)

label = bmi['label']

normal_weight = bmi['weight'] / 180
normal_height = bmi['height'] / 80

normal_data = pd.concat([normal_weight,normal_height], axis=1)

data_train, data_test, label_train, label_test = train_test_split(normal_data, label)

clf = svm.SVC(gamma='auto')
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

score = metrics.accuracy_score(label_test, predict)
report = metrics.classification_report(label_test, predict)

print('정답률: %s%% '%round(score*100,2))
print(report)