import random

def calc_bmi(h,w):
    bmi= w / (h/100) **2
    if bmi <18.5:
        return 'Tine' + '\n'
    elif bmi < 25:
        return 'Normal' + '\n'
    else:
        return 'Fat' + '\n'

data = []
data_num=30000
index='height,weight,label\n'
data.append(index)
for i in range(data_num):
    w= random.randint(35,80)
    h= random.randint(120,180)

    data.append(str(h)+','+str(w)+','+calc_bmi(h,w))


with open('bmi.csv','w',encoding='utf-8') as f:
    f.writelines(data)

print('ok %s개'%data_num)

