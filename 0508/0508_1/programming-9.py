s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

result = []

for ch in s1:
    if ch in s2 and ch not in result:
        result.append(ch)

print("모두 포함된 글자:", "".join(result))

#360p 9번문제