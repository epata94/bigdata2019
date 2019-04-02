import random

def calc_bmi (he, we) :
    bmi = we / (he/100) ** 2
    if bmi < 18.5 : return 'Thin'
    elif 18.5 <= bmi < 25 : return 'Normal'
    else : return 'Fat'

bmi_file = open('bmi.csv', 'w', encoding='utf-8')
bmi_file.write("height,weight,label\r\n")

for idx in range(30000) :
    he = random.randint(120, 200)
    we = random.randint(35, 80)
    label = calc_bmi(he, we)
    bmi_file.write("%s, %s, %s\r\n" %(he, we, label))

bmi_file.close()