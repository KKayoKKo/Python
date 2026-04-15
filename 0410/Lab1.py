def main() :
    print("20cm 피자 2개의 면적:", get_area(20)+get_area(20))
    print("30cm 피자 1개의 면적:", get_area(30))

def get_area(radius) :
    if radius > 0 : # 반지름이 0보다 큰지 확인
        area = 3.14*radius**2 # 반지름이 양수이면 원의 면적 계산 (πr²)
    else :
        area = 0
    return area

main()

#  피자 크기 비교 랩 