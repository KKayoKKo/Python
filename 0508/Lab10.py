sentence = input("문자열을 입력하시오: ")

table = {"alphas": 0, "digits": 0, "spaces": 0} # 딕셔너리 초기화

for i in sentence:
    if i.isalpha(): # 카운트 증가
        table["alphas"] += 1

    if i.isdigit(): # 카운트 증가
        table["digits"] += 1

    if i.isspace(): # 카운트 증가
        table["spaces"] += 1

print(table)