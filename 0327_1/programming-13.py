for num in range(2, 21):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num, end=" ")
# 2부터 20까지의 소수를 출력하는 프로그램 p200