n = int(input("몇 번째 항을 구할까요? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    temp = a + b
    a = b
    b = temp
    
# 피보나치 수열의 n번째 항을 구하는 프로그램 p200