word_list = ['aba', 'xyz', 'abc', '121']
result = 0

for item in word_list:
    if item[0] == item[-1]:
        result = result + 1

print(word_list)
print("문자열의 개수 =", result)

# P301 5번 문제