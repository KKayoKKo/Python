board_size = int(input("게임판의 크기: "))

for row in range(board_size):
    print("----" * board_size)

    for col in range(board_size):
        print("|   ", end="")
    print("|")

print("----" * board_size)

# 게임판을 출력하는 프로그램 p201