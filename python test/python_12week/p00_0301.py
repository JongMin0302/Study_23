# 문제 P00-0301
"""
1부터 100까지 자연수(100개) 의 
평균,표준편차,분산,최대값,최소값 5개를 모두 출력하시오

- 조건
    - 입력값이 1부터 100 이외의 값인 경우에도 정상 
    동작하도록 계산식에 상수를 직접 사용하지 않는다.
    - 오답 :  (1+100)/2 (x) , avg = sum/100 (x)
    - **방법1) for문을 사용하시오.**
    - **방법2) numpy 를 이용하시오**
"""
numbers = list(range(1, 101)) 

# 평균 계산
total = sum(numbers)
avg = sum(numbers) / len(numbers)

# 표준편차 및 분산 계산
squared_diff = [(x - avg) ** 2 for x in numbers]
variance = sum(squared_diff) / len(numbers)
std_deviation = variance ** 0.5

# 최대값 및 최소값 계산
max_value = max(numbers)
min_value = min(numbers)

#소수점 자리 바꾸기
deviation = round(std_deviation, 2)

# 결과 출력
print("평균:", avg)
print("총합:", total)
print("표준편차:", deviation)
print("분산:", variance)
print("최대값:", max_value)
print("최소값:", min_value)

print()
#방법 2
##############################################
import numpy as np

numbers = np.arange(1, 101)  # 1부터 100까지 자연수 배열 생성
print(numbers)
total = np.sum(numbers)

# 평균 계산
avg = np.mean(numbers)

# 표준편차 및 분산 계산
std_deviation = np.std(numbers)
variance = np.var(numbers)

# 최대값 및 최소값 계산
max_value = np.max(numbers)
min_value = np.min(numbers)

#소수점 자리 바꾸기
deviation = round(std_deviation, 2)

# 결과 출력
print("평균:", avg)
print("총합:", total)
print("표준편차:", deviation)
print("분산:", variance)
print("최대값:", max_value)
print("최소값:", min_value)


