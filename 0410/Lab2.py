def display(msg, count=1) : # count=1 → 기본값이 1인 매개변수 (값을 안 주면 1번 출력)
        for k in range(count) :
                    print(msg)
                    
display("환영합니다.", 5)  # "환영합니다."를 5번 출력하라는 의미

# 환영 문자열 출력 함수 랩
# 문자열을 원하는 횟수만큼 반복 출력하는 함수