try:
    result = 4/2
    print(result)
    f=open("NA.txt","r")
    f.close()
except Exception as e:
# 모든 Failure를 동일하게 처리하고 싶을고 Exception의 유형을 정확이 모를 때
# 유용하다. (일반적인 상황에서 적용할 수 있는 Tip)
    print(e)

print("Program End")
