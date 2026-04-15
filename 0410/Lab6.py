# 구조화 프로그래밍 실습 랩 1

def menu():
    print("1. 섭씨 온도->화씨 온도")
    print("2. 화씨 온도->섭씨 온도")
    print("3. 종료")
    selection = int(input("메뉴를 선택하세요: "))
    return selection


def ctof(c): # 섭씨 → 화씨 변환 함수
    temp = c * 9.0 / 5.0 + 32
    return temp
# 화씨 = 섭씨 × 9/5 + 32


def ftoc(f): # 화씨 → 섭씨 변환 함수
    temp = (f - 32.0) * 5.0 / 9.0
    return temp
# 섭씨 = (화씨 - 32) × 5/9

def input_f():
    f = float(input("화씨 온도를 입력하시오: "))
    return f

# 온도 변환(섭씨↔화씨)을 메뉴 기반으로 처리하기 위한 함수