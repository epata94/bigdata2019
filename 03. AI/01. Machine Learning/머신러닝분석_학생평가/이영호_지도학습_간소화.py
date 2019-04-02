from sklearn import svm, metrics, model_selection
import pandas as pd

# iris.csv 파일을 읽는다.
iris_file = pd.read_csv('iris.csv')
# 고정변수를 iris_data로 분리
iris_data = iris_file[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
# 종속변수를 iris_label로 분리
iris_label = iris_file["Name"]

# 머신 러닝 모델을 생성한다.
clf = svm.SVC()

# 훈련 데이터와 테스트 데이터로 분할
scores = model_selection.cross_val_score(clf)

print("각각의 정답률", scores)
