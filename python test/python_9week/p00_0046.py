### 문제 P00-0046
'''
n개의 숫자를 입력받고 입력값의 합을 출력하시오

- 조건
    - for 반복문사용
'''
nn = input()
lt = nn.split()
print(lt)

sum1 = 0
for kk in lt:
  sum1 += int(kk) 
print(sum1)


