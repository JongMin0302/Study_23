### 문제 P00-0011

# 다음 코드는 Hello World 를 3번 출력하는 
# 프로그램의 일부이다. 프로그램을 추가해서 완성하시오

# - 조건
# str1 = "Hello World"

# for kk in range(5,50,3):
#   if :
#     break
#   else:
#     print(str1)


str1 = "Hello World"
flag = False
for kk in range(5,50,3):
  if kk>13:
        flag = True
  if flag:
        break
  else:
        print(str1)