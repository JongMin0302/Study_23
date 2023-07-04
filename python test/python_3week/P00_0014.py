### 문제 P00-0014

# 1부터 20까지 정수중 짝수를 출력하시오

# - 조건
#     - 리스트를 이용해서 출력하시오

#for문을 이용한다
#if문을 이용하여 짝수만 출력한다
lt=[]
for kk in range(1,21):
    if kk%2==0:
        lt.append(kk)
print(str(lt).replace(',' , ' '))
