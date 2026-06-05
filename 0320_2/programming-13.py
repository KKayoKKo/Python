a = int(input("연도를 입력하세요: "))

if (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0)):
    print(f"{a}년은 윤년입니다.")
else:
    print(f"{a}년은 평년입니다.")
    
# 윤년 판단 프로그램 152p