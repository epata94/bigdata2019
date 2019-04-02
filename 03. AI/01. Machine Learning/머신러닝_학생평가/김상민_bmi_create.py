import random

def calculation_bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        return "Thin"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    else:
        return "Fat"

file_bmi = open('bmi.csv', 'w', encoding='utf-8')
file_bmi.write('height,weight,label\r\n')
random_data_count = {"Thin": 0, "Normal": 0, "Fat": 0}
for random_data in range(30000):
    random_height = random.randint(120, 180)
    random_weight = random.randint(35, 80)
    label = calculation_bmi(random_height, random_weight)
    random_data_count[label] += 1
    file_bmi.write("{0},{1},{2}\r\n".format(random_height, random_weight, label))

file_bmi.close()
print("랜덤 데이터 생성 완료", random_data_count)