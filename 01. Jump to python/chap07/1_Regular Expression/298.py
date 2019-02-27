import re
p=re.compile('[abc]')
m = p.match("a")
print(m) # 매칭이 된다
p=re.compile('[abc]')
m = p.match("k") # 매칭이 안된다.
print(m)
p=re.compile('[abc]')
m = p.match("before") # 첫글자에 b가 있어서 매칭
print(m)
p=re.compile('[abc]')
m = p.match("dude") # 첫글자에 문자열 클래스에 있는 a,b,c가 모두 없기 때문에
print(m)
p=re.compile("[abc]")
m = p.match("dad") # 첫번째 글자에 abc가 없어서 매칭이 안된다.
                    # 두번째 글자가 문자열 클래스에 있으나 첫번째가 아니기 때문에
                    # 매칭이 안된다.
print(m)
p=re.compile("[def]")
m = p.match("dad") # 첫번째 글자가 정규식 문자열 클래스에 포함되어 있어서 매칭
print(m)
p=re.compile("d[def]") # 첫번째 글자 d는 매칭이 되나 두번쨰 글자는 매칭이 되지 않는다.
                        # 정규식의 100%가 매칭이 되어야 반환 되기 때문에 매칭이 안된다.
m = p.match("dad")
print(m)
p=re.compile("d[abc]") #문자열을 기준으로는 dad의 세번째 글자 d와 매칭이 되지는 않으나
                        #정규식을 기준으로는 d 그리고 [abc] 두 조건이 100% 매치가
                        #'da'로 되기 때문에 매칭이 된다.
m = p.match("dad")
print(m)
p=re.compile("d[abc]a") #정규식을 기준으로 두번째까지는 매칭이 되나 세번쨰가 매칭이 되지
                        # 안는다.
m = p.match("dad")
print(m)

p=re.compile("[abc]d") # 문자열 ad는 정규식 패턴에 맞게 보일수 있으나 정규식의 순서와
                       # 맞지 안으므로 매칭이 되지 안는다.
m = p.match("dad")
print(m)
p=re.compile("[cd][ab]") # 첫글자가 c,d 중에 하나이고 두번째 글자가 a,b중에 하나인 정규식
                          # 이므로 매칭이 된다.
m = p.match("da")
print(m)
