N_PRIMES = 50 # 찾아야 하는 소수 개수.
number = 2 # 2 부터 시작.
count = 0

while count < N_PRIMES:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1

    if prime:  # 소수이면 소수 개수를 증가, 출력함.
        count += 1
        print(number, end=" ")

    number += 1
# 소수 찾기 랩