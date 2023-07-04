### 문제 P00-0071
"""
가변인자를 이용해서 입력값 모두의 합을 
출력해주는 함수 sum_all() 를 만드시오.
"""
## 코드 작성  ############
def sum_all(*args, **a):
    total = sum(args)
    
    for key,value in a.items():
        total += value
    print('합 : ',total)

#######################

sum_all(eng=99, kor=90)
