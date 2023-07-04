# 문제 P00-0302
"""
1부터 100까지 자연수(100개) 의 
평균,표준편차,분산,최대값,최소값,**중간값**
6개를 모두 출력하시오

- 조건
    - 입력값이 1부터 100 이외의 값인 경우에도 정상 
    동작하도록 계산식에 상수를 직접 사용하지 않는다.
    - 입력값이 랜덤하게 중복해서 섞여있을 수 있다.
    - **방법1 : for문을 사용하시오.**
        - sorted() 함수를 사용
    - **방법2 : numpy 이용**
"""
import numpy as np

num = int(input())
list = [i+1 for i in range(num)]
print(list)
# 평균 계산
avg = np.mean(list)

# 표준편차 및 분산 계산
std_deviation = np.std(list)
variance = np.var(list)

# 최대값 및 최소값 계산
max_value = np.max(list)
min_value = np.min(list)

# 중간값 계산
middle_value = np.median(list)

# 결과 출력
print("평균:", avg)
print("표준편차:", std_deviation)
print("분산:", variance)
print("최대값:", max_value)
print("최소값:", min_value)
print("중간값:", middle_value)

#방법 2
import numpy as np

num = int(input())
list = [i+1 for i in range(num)]

list.sort()
list = sorted(list)

# 평균 계산
avg = np.mean(list)

# 표준편차 및 분산 계산
std_deviation = np.std(list)
variance = np.var(list)

# 최대값 및 최소값 계산
max_value = np.max(list)
min_value = np.min(list)

# 중간값 계산
middle_value = np.median(list)

# 결과 출력
print("평균:", avg)
print("표준편차:", std_deviation)
print("분산:", variance)
print("최대값:", max_value)
print("최소값:", min_value)
print("중간값:", middle_value)

