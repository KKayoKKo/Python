country = input("배송지(현재는 한국과 미국만가능): ")
price = int(input("상품의가격: "))

if country == "한국":
    if price >= 20000:
        shippingcost= 0
    else:
       shippingcost= 3000
else:
    if price >= 100000:
            shippingcost= 0
    else:
            shippingcost= 8000
 
print("배송비= ",shippingcost)