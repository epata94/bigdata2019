f=open("./file3.txt",'r',encoding='UTF-8')
line = ' '
while line:
    line = f.readline()
    print(line,end='') #원본에 \n이 있기 때문에 그대로 출력하려면 end='' 추가
f.close()