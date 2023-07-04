### 문제 P00-0070
"""
가변인자를 이용해서 입력값 모두의 합을 
출력해주는 함수 sum_all() 를 만드시오.
"""
## 코드 작성  ############
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

#######################
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
