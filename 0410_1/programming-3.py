def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))

a, b, c, d = calc(num1, num2)

print(a, b, c, d, "이 반환되었습니다.")