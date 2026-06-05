import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operator = random.randint(1, 4)

if operator == 1:
    result = num1 + num2
    symbol = '+'

elif operator == 2:
    result = num1 - num2
    symbol = '-'

elif operator == 3:
    result = num1 * num2
    symbol = '*'

else:
    result = num1 / num2
    symbol = '/'

answer = float(input(f"{num1} {symbol} {num2}의 값은? "))

if answer == result:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
    
# 덧셈 퀴즈를 자동으로 생성, 덧셈, 뺄셈, 곱셈, 나눗셈 하나 선택
# 사용자의 답 자동 채점 151p