def getSorted(x, y):
    if x < y:
        return x, y
    else:
        return y, x

num1 = int(input("첫 번째 정수: "))
num2 = int(input("두 번째 정수: "))

a, b = getSorted(num1, num2)

print(a, b)

# 248p 2개의 정수를 크기 순으로 반환하는 함수 getSorted(x,y)를 작성