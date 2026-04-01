divisor = 1.0 # 나누는 수 (분모)
divident = 4.0 # 나눠지는 수 (분자)
sum = 0.0 # 결과를 누적하는 변수 (합계)

loop_count = int(input("반복횟수: "))

while loop_count > 0:
    sum = sum + divident / divisor
    divident = -1.0 * divident
    divisor = divisor + 2
    loop_count = loop_count - 1

print("Pi = %f" % sum)

#4/1 - 4/3 + 4/5 - 4/7 ... 를 계속 더해서 π를 구하는 코드
# 파이 계산하기 랩