# 문제 P00-0806
"""
다음 프로그램은 lt1 의 원소를 삭제하는 프로그램의 일부이다.

아래 코드는 ‘AAA’ 원소를 삭제하는 경우 ‘AAA’ 모든
 원소가 삭제되지 않는 오류가 있다.

코드 내용을 수정해서 올바른 입출력을 갖는 프로그램을 작성하시오.

- 조건
    - Jupyterlab 을 이용하시오.
    - (방법1) for 문을 사용하지 말것
    - (방법2) for 문을 사용할것
"""
lt1 = ['BBB','AAA','AAA'] 


def delete_List():
  print(lt1)
  key = input('Delete Data :') 

 
  if set(lt1) & {key} == set(): 
    print(f'[{key}] No data in list')
    return    
  

  while(key in lt1):
    lt1.remove(key) 
  print(lt1)
  
delete_List()

# Case 2
lt1 = ['BBB','AAA','AAA'] 


def delete_List():
    print(lt1)
    key = input('Delete Data :') 

 
    if set(lt1) & {key} == set(): 
        print(f'[{key}] No data in list')
        return    


    for kk in reversed(range(len(lt1))):
        if lt1[kk] == key:
            del lt1[kk] 
    print(lt1)
  
delete_List()