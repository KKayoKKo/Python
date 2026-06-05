weight = float(input("무게(킬로그램): "))
height = float(input("키(미터): "))

bmi = weight / (height ** 2)

print(f"당신의 BMI: {bmi}")

if bmi < 25:
    print("정상입니다.")
elif bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")
    
# BMI 계산 프로그램 152p