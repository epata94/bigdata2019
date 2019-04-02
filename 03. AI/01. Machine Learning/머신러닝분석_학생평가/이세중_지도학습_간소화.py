from sklearn import svm, metrics, model_selection
import pandas as pd
dt = pd.read_csv("iris.csv") # 데이터로드
data = dt[["SepalLength","SepalWidth","PetalLength","PetalWidth"]] # 고정변수
label = dt["Name"]                                                      # 종속변수 분리
clf = svm.SVC() #머신 러닝 모델 생성
score = model_selection.cross_val_score(clf, data, label, cv=5) #학습 및 테스트 전용 데이터 나누기 & 크로스 벨리데이션 하기
print("각각의 정답률 :"+str(score))
print("평균 정답률 :"+str(score.mean()))
