### 문제 P00-0004

# Hello World 문자열의 짝수번째 문자를 
# ‘_’ 으로 변환해서 출력하시오

# - 조건
#     - for 반복문 사용
#     - enumerate 를 사용하시오
r = ""
for kk,aa in enumerate("Hello World"):
    if kk %2==1:
        r += "_"
    else:
        r += aa
print(r)
    