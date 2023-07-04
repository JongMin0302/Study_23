'''
lt2 = [(3,4),(5,6),(7,8)] 를 정의하고,  출력형태가  
[7,11,15] 이 되도록 프로그램 하시오.

- 조건
    - 함수 2개 이상을 만들서 문제를 해결하시오.
    - Myadd2(), Myadd4()'''

lt2 = [(3,4),(5,6),(7,8)] 

def Myadd2(x_tu):
  return x_tu[0] + x_tu[1]
  
def Myadd4(x_lt):
  lt = []
  for kk in x_lt:
    lt.append(Myadd2(kk))
  return lt

print(Myadd4(lt2))


