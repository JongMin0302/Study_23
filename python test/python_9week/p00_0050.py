### 문제 P00-0050
'''
1개의 문자열을 입력받고, 공백을 기준으로 
문자열을 행단위로 출력하시오

- 조건
    - for 반복문사용
    - join() replace() split() 문자열 관련 
    함수를 사용하지 않는다.
'''
#input함수로 문자열 입력받는다
#for문에 하나하나 넣는다 
#그 다음 공백을 만날경우에 

# a = input()
# for kk in a:
#     if kk == ' ':
#         print()
#     else:
#         print(kk,end ='')

nn = input()
lt1 = []
str1 = ""
for kk in nn:
  if kk != " ": #내용이 있다면
    str1 += kk  #임시문자열을 만들어가고
  else:         #공백이라면,
    if str1 != "": #str1에 내용이 있다면
        lt1.append(str1) #그동안 쌓인 문자열을 등록
        str1 = ""   # 주의~~ 임시문자열 초기화
lt1.append(str1) #주의~ 마지막 문자열 입력해야함
print(lt1)
for kk in lt1:
  print(kk)


