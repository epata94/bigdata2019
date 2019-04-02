from sklearn import svm, metrics, model_selection
import pandas as pd

# iris.csv 파일을 읽는다.
iris_file = pd.read_csv('iris.csv')
# 고정변수를 iris_data로 분리
iris_data = iris_file[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
# 종속변수를 iris_label로 분리
iris_label = iris_file["Name"]

# 머신 러닝 모델을 생성한다.
clf = svm.SVC(gamma='auto')

# 훈련 데이터와 테스트 데이터로 분할하여 훈련 데이터를 활용해 학습하고, 테스트 데이터로  테스트해서 학습의 타당성을 검증한다.
# 이 때, 빅데이터를 5등 분할하여 한 집합을 테스트 전용 데이터, 나머지 집합을 훈련 전용 데이터로 하여 총 5가지 정답률을 구해
# 그 평균을 구하여 평균 정답률을 구한다.
scores = model_selection.cross_val_score(clf, iris_data, iris_label, cv=5)

print("각각의 정답률", scores)
print("평균 정답률 = %.3f" %scores.mean())