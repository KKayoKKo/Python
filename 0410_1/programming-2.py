def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))

print("(", num1, "+", num2, ") =", add(num1, num2))
print("(", num1, "-", num2, ") =", sub(num1, num2))
print("(", num1, "*", num2, ") =", mul(num1, num2))
print("(", num1, "/", num2, ") =", div(num1, num2))

# 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 작성 p246