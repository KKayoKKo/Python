import random

board = []

for i in range(10):
    row = []
    for j in range(10):
        if random.random() < 0.3:
            row.append('#')
        else:
            row.append('.')
    board.append(row)

for r in board:
    print(" ".join(r))
    
# p304 14번 문제