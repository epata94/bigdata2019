from sklearn import svm,model_selection
import pandas as pd

# 데이터 로드
iris_csv = pd.read_csv('iris.csv')

# 고정변수, 종속변수 분리
data = iris_csv[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label = iris_csv['Name']

# 머신 러닝 모델 생성
svm_model = svm.SVC(gamma='auto')
# 크로스 밸리데이션 하기( 학습 및 테스트 전용 데이터 나눠줌 )
score = model_selection.cross_val_score(svm_model,data,label,cv=5)
print('각각 정답률 =',score)
print('평균 정답률 =',score.mean())