nums = list(range(2, 101))
result = []

for i in nums:
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        result.append(i)

print(result)

# p305 16번 문제