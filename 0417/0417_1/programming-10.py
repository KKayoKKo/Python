seat_map = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    seat_map.append(row)

while True:
    print("--------------------")
    print("  1 2 3 4 5 6 7 8 9 10")
    print("--------------------")

    for r in seat_map:
        print(*r)

    row_num = int(input("원하시는 좌석의 행번호(종료 -1): "))
    if row_num == -1:
        break

    col_num = int(input("원하시는 좌석의 열번호(종료 -1): "))
    if col_num == -1:
        break

    if seat_map[row_num - 1][col_num - 1] == 0:
        seat_map[row_num - 1][col_num - 1] = 1
        print("예약되었습니다.")
    else:
        print("이미 예약된 좌석입니다.")
        
# p304 13번 문제