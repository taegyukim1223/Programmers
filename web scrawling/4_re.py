import re

#ca?e

p = re.compile('ca.e') 

m = p.match("case")
#주어진 문자열이 앞에서부터 읽어서 일치하면 T아니면 F

# print(m.group()) # 매칭안되면 에러
if m :
    print(m.group()) # 일치하는 문자열 반환
    print(m.string) # 입력받은 문자열 
    print(m.start())
    print(m.end())
    print(m.span()) # 시작과 끝 인덱스 반환
else :
    print("매칭x")

m = p.search("good care")

listm = p.findall("careless") # 일치하는 모든 것을 리스트로 반환,
print(listm)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 비교할 문자열과 처음부터 일치하는지 확인
# 3. m = p.search("비교할문자열") : 비교할 문자열중에 일치하는게 있는지 확인
# 4. listm = p.findall("비교할 문자열") : 비교할 문자열에서 일치하는 모든 것을 리스트 형태로 반환

# . : 하나의 문자를 의미
# ^ : 문자열의 시작을 의미 (^de) -desk -destination
# $ : (se$) : 문자열의 끝을 의미 -case -base / face(x)

