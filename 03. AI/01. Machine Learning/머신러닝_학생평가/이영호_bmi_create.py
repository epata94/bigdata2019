import random

def calc_bmi(h,w):
    bmi = w/(h/100)**2
    if bmi < 18.5 : return "Thin"
    if bmi < 24 : return "Normal"
    return "Fat"

fp = open("bmi.csv",'w',encoding="utf-8")
fp.write("height,weight,label\n")

for a in range(30000):
    h = random.randint(120,180)
    w = random.randint(35,80)
    x = calc_bmi(h,w)
    fp.write(str(h)+","+str(w)+","+x+"\n")

fp.close()
