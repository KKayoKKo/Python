a = float(input("a를 입력하세요: "))
b = float(input("b를 입력하세요: "))
c = float(input("c를 입력하세요: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"실근은 {root1}과 {root2}입니다.")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"중근은 {root}입니다.")
else:
    print("실근이 존재하지 않습니다.")
    
# 이차방정식의 근 계산 프로그램 153p    