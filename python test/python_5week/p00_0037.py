### 문제 P00-0037
'''
1개의 문자열을 입력받고, Hello World 를 n 번 출력하시오

- 조건
    - for 반복문사용''' 


a = int(input())

'''
for kk in reversed(range(a)):
    print(kk+1,"Hello World")
'''

for kk in range(a):
    print(a-(kk),"Hello World")