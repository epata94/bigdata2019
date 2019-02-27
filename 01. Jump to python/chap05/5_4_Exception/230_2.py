try:
    result = 4/0
    print(result)
except ZeroDivisionError:
    print("비정상 종료")

print("Program End")
