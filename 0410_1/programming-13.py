import random

def dicegame():
    print("========== dicegame() 호출 ==========")

    human = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("인간: 주사위값 =", human)
    print("컴퓨터: 주사위값 =", computer)

    if human > computer:
        print("인간승리")
    elif human < computer:
        print("컴퓨터승리")
    else:
        print("무승부")

    print("========== dicegame() 복귀 ==========")

while True:
    dicegame()

    choice = input("중단할까요? Y/N: ")

    if choice == "Y" or choice == "y":
        break
    
# 인간과 컴퓨터가 주사위 게임을 하느 프로그램 p248