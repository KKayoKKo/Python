def testPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(2, 101):
    if testPrime(num):
        print(num, end=" ")
        
# 주어진 정수가 소수인지 검사하는함수 testPrime(n)를 작성 p247