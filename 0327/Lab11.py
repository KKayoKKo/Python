import random

initial_money = 50 #시작 돈
goal = 250 # 목표인 금액
wins = 0 # 성공 횟수

for i in range(100):  # 도박장에 100번 감.
    cash = initial_money

    while cash > 0 and cash < goal:  # 돈이 0이거나 목표 도달하면 종료함.
        number = random.randint(1, 2)

        if number == 1:
            cash = cash + 1  # 1달러 획득.
        else:
            cash = cash - 1  # 1달러 손실.

    if cash == goal:
        wins = wins + 1 # 목표 도달하면 성공 카운트

print("초기금액 $%d" % initial_money)
print("목표금액 $%d" % goal)
print("100번 중에서 %d번 성공" % wins)

# 도박상의 확률 랩.