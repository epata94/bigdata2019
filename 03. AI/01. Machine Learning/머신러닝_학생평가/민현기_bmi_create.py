import pandas as pd
import random

def label_create(height, weight):
    bmi = weight / (height/100) ** 2
    if bmi < 18.5: return 'Thin'
    if bmi < 25: return 'Normal'
    return 'Fat'

bmi_data = pd.DataFrame(columns=('height', 'weight', 'label'))

for i in range(30000):
    height = random.randint(120,180)
    weight = random.randint(35,80)
    bmi_data.loc[i] = [height, weight, label_create(height, weight)]

bmi_data.to_csv('bmi.csv', index=False)
