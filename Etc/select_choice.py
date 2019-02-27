import random
class_member_list=['현구','상민','치우','현기','규동','민선','세중','영호','정헌']
group_number=1
index = 0
while True:
    if index == 0 or index % 3 ==0 and group_number < 4:
        print("="*10+" %d조 "%group_number+"="*10)
        group_number+=1
    try:
        current_number = len(class_member_list)
        print(class_member_list.pop(random.randint(0,current_number-1)))
        index+=1
    except:
        break
