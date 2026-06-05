number = int(input("정수를 입력하시오: "))

print("약수:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
        
# 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램 198p