import pandas as pd
from sklearn import svm, metrics, model_selection

# 데이터 로드
iris_data = pd.read_csv('iris.csv')

# 고정 변수, 종속 변수 분리
data = iris_data[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
label = iris_data['Name']

# 머신 러닝 모델 생성
clf = svm.SVC(gamma='auto')

# 크로스 벨리데이션 하기
scores = model_selection.cross_val_score(clf, data, label, cv=5)

# 출력
print("각각의 정답률 : ", scores)
print("평균 정답률 : ", scores.mean())