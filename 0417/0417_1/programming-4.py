list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = []

for i in list_1:
    if 3 <= i <= 8:
        list_2.append(-i)
    else:
        list_2.append(i)

print("실행전", list_1)
print("실행후", list_2)

# p301 4번 문제