n = int(input("n의 값을 입력하시오: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i**2

print("계산값은", sum, "입니다.")   

#1부터 n까지의 제곱의 합을 계산하는 프로그램 p199