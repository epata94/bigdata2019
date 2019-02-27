import re
file_name_list=["foo.bar","autoexec.bat","sendmail.cf"]

# 확장자가 bat인 파일은 제외해야 하는 조건 추가
p = re.compile('.*[.][^b].*$')
for file_name in file_name_list:
    print(p.search(file_name))
# 수행 결과: foo.bar 도 같이 필터링 되기 때문에 실패한 조건
# None
# None
# <re.Match object; span=(0, 11), match='sendmail.cf'>