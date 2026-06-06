num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))

if num1 < num2:
    small = num1
else:
    small = num2

for i in range(small, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(num1, "와", num2, "의 최대공약수는", i, "입니다.")
        break
    
# 최대공약수를 구하는 프로그램 p199
