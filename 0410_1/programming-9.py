def gcd(a, b):
    if a < b:
        small = a
    else:
        small = b

    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

num1 = int(input("첫 번째 정수: "))
num2 = int(input("두 번째 정수: "))

print(gcd(num1, num2))

# 사용자로부터 두개의 정수를 입력받아서 최대 공약수를 찾는 함수 p247