### 문제 P00-0048
'''
n개의 숫자를 입력받고 입력값의 
합을 출력하시오

- 조건
    - for. while 반복문사용 x
- 입력
    - 입력은 스페이스로 구분한다.
'''
#방법 1
nn = input() #문자열 입력            
lt = nn.split( ) #문자->리스트

print(sum(map(int,lt)))
# lt = map(int, lt)
# lt = list(lt)
# lt = sum(lt)
# print(lt)
# lt2 = [1,2,3,4]
# print(sum(lt2)) sum은 리스트에도 적용된다
#map 함수로 lt 릏 int형으로 만든다음
#다시 list를 써서 리스트로 변환시켜 sum으로 더했다

#방법 2 eval함수 사용
a = input()
a = a.replace(" ", "+")
print(eval(a))
#input된 숫자에 replace함수를 이용하여 공백을 +로 바꿈
#그 이후 문자열이여도 계산식이 성립되면 계산해주는  eval
#함수로 계산된 값을 출력함








