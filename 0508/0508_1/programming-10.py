set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}

result = set()

for x in set1:
    if x not in set2:
        result.add(x)

for x in set2:
    if x not in set1:
        result.add(x)

print("어느 한쪽에만 있는 요소들", result)

#p361 10번 문제