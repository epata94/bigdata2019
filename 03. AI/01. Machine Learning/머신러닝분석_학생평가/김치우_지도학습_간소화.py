import pandas as pd # 고정변수, 종속변수 분리를 위한 pandas 프레임워크 활용
from sklearn import svm, metrics, model_selection # sklearn:

csv = pd.read_csv('iris.csv')
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv[["Name"]]
clf = svm.SVC()
corrects = model_selection.cross_val_score(clf, data, label, cv=5)

print("각각의 정답률 =", corrects)
print("평균 정답률 =", corrects.average())