### 문제 P00-0013 continue 사용

# 1부터 20까지 정수중 홀수를 출력하시오

# - 조건
#     - continue 사용

#1~20 까지의 정수를 for문에 넣는다
#그 이후 if 문을 이용하여 홀수가 아닐경우 
#kk가 출력되자 않게 continue 문을 사용한다
for kk in range(1,21):
    if kk%2 == 0:
        continue
    print(kk,end=" ")
    