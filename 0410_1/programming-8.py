def getMoneyText(amount):
    num = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

    result = ""

    hundred = amount // 100
    ten = (amount % 100) // 10
    one = amount % 10

    if hundred > 0:
        result = result + num[hundred] + "백 "

    if ten > 0:
        result = result + num[ten] + "십 "

    if one > 0:
        result = result + num[one]

    result = result + "원"

    return result

money = int(input("1000이하의 금액을 입력하시오: "))
print(getMoneyText(money))

# 247p 8번 문제