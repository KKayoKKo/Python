def sum(a, b, c): # 매개변수 3개 (a, b, c)를 받음
            print(a + b + c) # 세 값을 더해서 출력
            
            
alist = [1, 2, 3] #리스트 생성
sum(*alist)


# *alist는 리스트를 풀어서 함수의 각각의 인자로 전달하는 역할