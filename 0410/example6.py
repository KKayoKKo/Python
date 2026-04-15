def factorial(n): # 팩토리얼 계산 함수 (n!)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) # n! = n × (n-1)!


n = eval(input("정수를 입력하시오: "))
print(n, "!= ", factorial(n))


# 순환호출의 예제