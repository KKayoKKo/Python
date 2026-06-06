n = int(input("입력할 값의 개수: "))

nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

total = sum(nums)

print("값의 합계 =", total)

# 사용자가 입력하는 정수값을 리스트에 저장하고 이 값을 합계를 계산 p301