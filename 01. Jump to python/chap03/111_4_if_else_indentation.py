# coding: cp949
is_cash=0
is_card=1

if is_cash+is_card: # 조건식을 사용한 경우
#print("택시를 타고 가라") # indentaion이 없기 때문에 Error
    print("유효한 결제 수단이 있습니다.")
    print("택시를 타고 가세요.")
#print("택시 출발합니다") # else 이전까지는 동일한 indentation 유지
else:
    print("걸어가세요.")

print("이용해 주셔서 감사합니다")
