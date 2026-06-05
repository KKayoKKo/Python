import random

player = int(input("선택하시오(1: 가위 2: 바위 3: 보) "))
computer = random.randint(1, 3)

print("컴퓨터의 선택:", computer)

if player == computer:
    print("비겼습니다.")

elif ((player == 1 and computer == 3) or
      (player == 2 and computer == 1) or
      (player == 3 and computer == 2)):
    print("사용자가 이겼음")

else:
    print("컴퓨터가 이겼음")
    
# 가위바위보 게임 p151