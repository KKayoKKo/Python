def checkPass(p):
    upper = 0
    lower = 0
    digit = 0

    for ch in p:
        if ch >= 'A' and ch <= 'Z':
            upper = 1
        elif ch >= 'a' and ch <= 'z':
            lower = 1
        elif ch >= '0' and ch <= '9':
            digit = 1

    if len(p) >= 8 and upper == 1 and lower == 1 and digit == 1:
        return True
    else:
        return False

while True:
    pw = input("패스워드를 입력하시오: ")

    if checkPass(pw):
        print("사용할 수 있습니다.")
        break
    else:
        print("사용할 수 없습니다. 다시 입력하세요!")
        
# 패스워드가 8자 이상이고, 대문자, 소문자, 숫자를 모두 포함하는지 검사하는 함수 checkPass(p)를 작성하고 테스트한다. p246