from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

bmi_data = pd.read_csv("bmi.csv")

bmi_data['height']=bmi_data['height']/180
bmi_data['weight']=bmi_data['weight']/80

all_data=bmi_data[['height','weight']]
all_label=bmi_data['label']

bmi_train,bmi_test,label_train,label_test = train_test_split(all_data,all_label)
clf=svm.SVC(gamma='auto')
clf.fit(bmi_train,label_train)
predit_label=clf.predict(bmi_test)

acc=metrics.accuracy_score(predit_label,label_test)
clas=metrics.classification_report(predit_label,label_test)

print("정답률:%.2f%%"%(acc*100))
print("리포트:",clas)



