grid = []

for i in range(3):
    layer = []
    for j in range(4):
        row = []
        for k in range(5):
            row.append('#')
        layer.append(row)
    grid.append(layer)

print(grid)

# p303 12번 문제