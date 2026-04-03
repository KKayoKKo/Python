def main() :
    print("20cm 피자 2개의 면적:", get_area(20)+get_area(20))
    print("30cm 피자 1개의 면적:", get_area(30)) 

# get_area(30) → 반지름이 30인 원의 면적
# get_area(20) → 반지름이 20인 원의 면적

def get_area(radius) :
    if radius > 0 :
        area = 3.14*radius**2
    else :
        area = 0
    return area
# 반지름이 0보다 크면 정상 계산, 아니면 0으로 처리.

main()

# 피자 크기 비교 랩 예제.