from sklearn import svm, metrics, model_selection
import pandas as pd

# 데이터 로드
iris = pd.read_csv('iris.csv')

# 고정변수, 종속변수 분리
data =iris[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
label = iris['Name']

# 머신러닝 모델 생성
clf = svm.SVC(gamma='auto')

# 크로스벨리 데이션하기
# 학습 및 테스트 전용 데이터 나누기
score = model_selection.cross_val_score(clf, data, label, cv=5)

print('각각의 정답률: ', score)
print('평균 정답률: ', score.mean())