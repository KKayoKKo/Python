price = int(input("정가를 입력하시오: ")) # 가격 입력
if price >= 100:
    dis_rate = 0.85
    print("10층에서 사은품을 받아가세요.")
else:
    dis_rate = 0.90

# 가격이 100 이상이면: 할인율: 0.85 → 즉, 15% 할인, 100 미만이면 할인율: 0.90 → 즉, 10% 할인

dis_price = dis_rate * price # 할인된 가격을 계산합니다.
print("할인된 상품의 가격=", dis_price)

# 세일 가격계산 랩