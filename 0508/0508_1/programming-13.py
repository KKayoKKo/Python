s = input("문자열을 입력하시오: ")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters = letters + 1
    elif ch.isdigit():
        digits = digits + 1

print("-> { \"LETTERS\":", letters, ", \"DIGITS\":", digits, "}")

#361p 13번 문제