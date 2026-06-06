coin = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]

print(coin)

max_count = 1
count = 1

for i in range(1, len(coin)):
    if coin[i] == coin[i - 1]:
        count = count + 1
    else:
        if count > max_count:
            max_count = count
        count = 1

if count > max_count:
    max_count = count

print("최대 연속 길이 =", max_count)

#p305 15번 문제