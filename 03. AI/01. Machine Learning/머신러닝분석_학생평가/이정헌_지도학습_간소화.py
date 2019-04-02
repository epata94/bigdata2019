from sklearn import svm, metrics, model_selection
import pandas as pd

#데이터 로드
iris_data=pd.read_csv("iris.csv")

#고정 변수 , 종속변수 분리
data=iris_data[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label=iris_data['Name']

#머신 러닝 모델 생성
clf=svm.SVC(gamma='auto')

# 크로스 밸리데이션 하기 총 5개의 구역으로 나누어
# 1번테스트 2,3,4,5번 학습 2번테스트 1,3,4,5번을 학습 이런식으로 5번을 반복함
scores=model_selection.cross_val_score(clf,data,label,cv=5)

print("정답률:",scores*100)
print("평균정답률:%.2f%%"%(scores.mean()*100))