import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

bmi = pd.read_csv('bmi.csv', header=0)

label = bmi['label']

normal_weight = bmi['weight'] / 180
normal_height = bmi['height'] / 80

normal_data = pd.concat([normal_weight,normal_height], axis=1)

data_train, data_test, label_train, label_test = train_test_split(normal_data, label)

