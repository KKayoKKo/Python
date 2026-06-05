num = int(input("정수= "))

a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = (num // 1000) % 10

sum = a + b + c + d

print(sum)

# 사용자로부터 4자리의 정수를 받아서 자리수의 합을 계산하는 프로그램 111p