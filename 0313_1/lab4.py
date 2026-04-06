weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

bmi = (weight / (height**2)) # height**2 → 키의 제곱, weight / (height**2) → BMI 값 계산
print("당신의 BMI=", bmi)

#  BMI 계산하기 랩