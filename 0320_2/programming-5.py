x, y, z = eval(input("3개의 정수를 입력하시오: "))

if x <= y and x <= z:
    smallest = x
elif y <= x and y <= z:
    smallest = y
else:
    smallest = z

print("제일 작은 정수는", smallest, "입니다.")

# 가장 작은 값 결정 p150