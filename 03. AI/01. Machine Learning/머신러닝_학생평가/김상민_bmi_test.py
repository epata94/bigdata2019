import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 데이터 불러오기
file_bmi = pd.read_csv('bmi.csv')

# 데이터 레이블 분류
label = file_bmi['label']
weight = file_bmi['weight'] / 80
height = file_bmi['height'] / 180  # 표준화
weight_and_height = pd.concat([weight, height], axis=1)

# 학습 데이터와 테스트 전용 데이터 분리
data_train, data_test, label_train, label_test = train_test_split(weight_and_height, label)

# 학습
clf_bmi = svm.SVC(gamma='auto')
clf_bmi.fit(data_train, label_train)

# 예측
predict_bmi = clf_bmi.predict(data_test)

# 결과
accuracy_score_bmi = metrics.accuracy_score(label_test, predict_bmi)
classification_report_bmi = metrics.classification_report(label_test, predict_bmi)

print("정답률(%%) : %s %%" % (accuracy_score_bmi*100))
print("리포트 : \n", classification_report_bmi)

