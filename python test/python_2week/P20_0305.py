# 문제 P20-0305

# 다음 그림과 같이 5각형을 거꾸로 그려보자. (시계방향)

# - 조건
#- 반복문 사용
#- 시계방향 회전
#- 왼쪽 아랫부분에서 시작
import turtle
aaa = turtle.Turtle()
a=5
b=360/5 
aaa.left(180-b)
for kk in range(a):
    aaa.forward(100)
    aaa.right(b)
