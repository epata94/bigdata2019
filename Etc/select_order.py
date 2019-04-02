import random
from time import sleep

index=1
class_member_list=['상민','치우','현기','규동','민선','세중','영호','정헌']
input("애들아~ 준비됬냐?\n")

while len(class_member_list)>0:
    print(str(index)+"번 발표자 => "+class_member_list.pop(random.randint(0,len(class_member_list)-1)))
    index+=1
    sleep(1)

