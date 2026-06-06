list_a = [1, 2, 3, 4, 5]
list_b = [1, 3, 3, 4, 5, 6, 7]

result = []

for i in list_a:
    if i in list_b:
        result.append(i)

print("결과 =", result)

# p302 8번 문제