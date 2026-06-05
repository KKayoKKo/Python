number = int(input("정수를 입력하시오: "))

for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

# 중첩 반목문 사용 p198