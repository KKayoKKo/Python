a = int(input("연도를 입력하시오: "))

zodiac = a % 12

if zodiac == 0:
    print("원숭이띠입니다.")
elif zodiac == 1:
    print("닭띠입니다.")
elif zodiac == 2:
    print("개띠입니다.")
elif zodiac == 3:
    print("돼지띠입니다.")
elif zodiac == 4:
    print("쥐띠입니다.")
elif zodiac == 5:
    print("소띠입니다.")
elif zodiac == 6:
    print("호랑이띠입니다.")
elif zodiac == 7:
    print("토끼띠입니다.")
elif zodiac == 8:
    print("용띠입니다.")
elif zodiac == 9:
    print("뱀띠입니다.")
elif zodiac == 10:
    print("말띠입니다.")
else:
    print("양띠입니다.")