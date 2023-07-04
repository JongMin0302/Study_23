### 문제 P00-0021

# input() 함수를 이용해서 숫자를 무한 입력받고, 
# 총합을 출력하고자 한다.

# - 조건
#     - = 을 입력받으면 총 합을 구한다.

#while문을 이용하여 여러번 입력 받는다
#입력받은 숫자를 빈 리스트에 넣는다
#-,=을 입력받으면 리스트 안에 모든숫자를 더하고 출력한다
#리스트를 초기화 한다
#그 이후 break를 건다
total = 0

while True:
    user_input = input()

    if user_input == '=' or user_input == '-':
        break
    
    print("+",user_input)
    number = int(user_input)
    total += number

print("sum:", total)
        
    
        


