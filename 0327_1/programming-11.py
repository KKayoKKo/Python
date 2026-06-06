import random

n = 10000000
count = 0

for i in range(n):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        count = count + 1

result = count / n * 4

print("파이의 값은", result, "입니다.")

# 몬테카를로 방법으로 파이의 값을 계산하는 프로그램 p200
