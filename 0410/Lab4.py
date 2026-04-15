def weeklyPay(rate, hour):
    money = 0
    if hour > 30:
        money = rate * 30 + 1.5 * rate * (hour - 30) # 기본급: rate × 30 # 1.5 × rate × (hour - 30)
    else: # 30시간 이하이면 그냥 시급 × 시간
        money = rate * hour 
    return money

rate = int(input("시급을 입력하시오:"))
hour = int(input("근무 시간을 입력하시오:"))
print("주급은 " + str(weeklyPay(rate, hour))) # 함수 결과를 문자열로 바꿔서 출력

# 주급 계산 프로그램
# 30시간까지는 기본 시급, 초과 근무는 1.5배로 계산하는 주급 계산 함수
