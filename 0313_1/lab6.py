itemPrice = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))
# 전부 int → 정수로 처리

change = note*1000 + coin500*500 + coin100*100 - itemPrice
# 내가 낸 돈 = (1000원×개수) + (500원×개수) + (100원×개수)
# 거스름돈 = 낸 돈 - 물건값

nCoin500 = change//500
change = change%500
# // → 몫 (몇 개 줄 수 있는지), % → 나머지

nCoin100 = change//100
change = change%100

nCoin10 = change//10
change = change%10

nCoin1 = change

print("500원=", nCoin500, "100원=", nCoin100, "10원=", nCoin10, "1원=", nCoin1)

# 자동판매기 프로그램 랩