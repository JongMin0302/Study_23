# 문제 P00-0805
"""
아래 코드는 데이터열 조작 CRUD 예제 중 일부이다. 

삭제할 문자열을 검색하고, 문자열을 삭제하는 
delete_List() 함수를 완성하시오.

- 조건
    - 검색하고자 하는 데이터열을 **집합**으로 바꾸고 
    delete_List() 함수를 완성하시오.
    - 지우려고 할 때 데이터가 없는 경우 에러 발생→ 
    데이터가 없다는 메시지 출력
    - 복수개의 데이터 삭제 불가 → 
    중복된 데이터가 있다면 함께 삭제 되어야 함
    - 방법 택1
    - 방법1 : 데이터가 없는 조건식을 **교집합**으로 판단
"""
lt1 = []  #데이터열 생성 Create

def append_List():
  key = input('Append Data :')
  lt1.append(key)
  print(lt1)
  
def print_List():
  print(lt1)
  pass

def delete_List():
    print(lt1)
    key = input('Delete Data :') #IO 처리 (2)

	#코드 추가 영역 ########
    while True:
        if set(lt1) & {key} != set(): 
            lt1.remove(key)
            if set(lt1) & {key} == set():
                break
        elif set(lt1) & {key} == set():
            print("no date")
            break

       
	##################
    
    print(lt1)

while True:
  print('1. Append List') #데이터열 조작(추가) Update
  print('2. Print List') #데이터열 읽기 Read
  print('3. Delete List') #데이터열 조작(검색+추가) Update
  print('4. Exit') 	#데이터열 삭제 Delete

  key = input('Select Number [1~4] :') #IO 처리 (1)
  if key == '1':
    append_List()
  elif key == '2':
    print_List()
  elif key == '3':
    delete_List()
  else:
    break

print('\nThanks.')