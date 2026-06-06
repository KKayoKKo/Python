list = [80, 20, 20, 30, 60, 30]

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)

new_list.sort()

print("주어진 리스트:", list)
print("정리된 리스트:", new_list)

#359p 1번 문제