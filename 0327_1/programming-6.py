import math

print("각도\tSin값\tCos값")

for degree in range(0, 91, 10):
    sin_value = math.sin(degree * math.pi / 180)
    cos_value = math.cos(degree * math.pi / 180)

    print(f"{degree}\t{sin_value:.3f}\t{cos_value:.3f}")
    
    # 0도부터 90도까지 10도 간격으로 sin cos을 출력하는 프로그램 p199