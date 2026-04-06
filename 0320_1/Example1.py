price = int(input("가격을 입력하시오: ")) # 정수 (금액)
card = input("카드 종류를 입력하시오: ") # 문자열 (카드 종류)

if price > 20000 and card == "kakao": # 가격이 20000원 초과이고 카드가 "kakao"이면 배송료 무료
    print("배송료가 없습니다.")
else:
    print("배송료는 3000원 입니다.")
 
 # 예제 배송료