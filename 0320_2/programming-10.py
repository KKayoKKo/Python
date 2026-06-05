fx = float(input("x의 값을 입력하시오: "))

if fx <= 0:
    result = fx**2 - 9*fx + 2
else:
    result = 7*fx + 2
print(f"f(x)의 값은 {result:.6f}")  

# 함수값 계산 P152