# 첫 번째 수 입력
x = int(input("첫 번째 수를 입력하시오: "))

# 두 번째 수 입력
y = int(input("두 번째 수를 입력하시오: "))

# 합 계산
plus = x + y

# 차 계산
minus = x - y

# 곱 계산
multi = x * y

# 평균 계산
avg = plus / 2

# 큰 수 구하기
big = max(x, y)

# 작은 수 구하기
small = min(x, y)

# 결과 출력
print("x :", x)
print("y :", y)
print("두 수의 합 :", plus)
print("두 수의 차 :", minus)
print("두 수의 곱 :", multi)
print("두 수의 평균 :", avg)
print("큰 수 :", big)
print("작은 수 :", small)


#110p 사용자로부터 두 개의 정수를 받아서 합, 차, 곱, 평, 큰수, 작은 수
#에 출력하는 프로그램을 작성하라. 파이썬이 제공하는 내장함수 이용