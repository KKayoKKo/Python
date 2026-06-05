weight, height = eval(input("체중과 키를 입력하시오: "))

standard_weight = (height - 100) * 0.9

if weight > standard_weight * 1.1:
    print("과체중입니다.")
elif weight < standard_weight * 0.9:
    print("저체중입니다.")
else:
    print("표준 체중입니다.")

# 저체중, 표준, 저체중 판단 프로그램 151p