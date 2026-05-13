def get_contact(): # 이름과 전화번호를 입력받아서 반환함.
    name = input("이름: ")
    number = input("전화번호: ")
    return name, number   # 튜플로 반환

def display_menu(): # 메뉴를 화면에 출력함.
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select


def main():
    address_book = {}   # 공백 딕셔너리 생성

    while True:
        user = display_menu()

        if user == 1:
            name, number = get_contact()
            address_book[name] = number   # 추가

        elif user == 2:
            name, number = get_contact()
            address_book.pop(name)        # 삭제

        elif user == 3:
            pass 

        elif user == 4:
            for key in sorted(address_book):
                print(key, "의 전화번호:", address_book[key])

        else:
            break


main()


# 연락처 관리 Lab