def get_info():
        name = input("이름:")
        age = int(input("나이:"))
        return name, age # 이름과 나이를 2개 값으로 동시에 반환
    
st_name, st_age = get_info() # 함수가 반환한 (name, age)를 각각 변수에 나눠 저장
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")

# 여러 개의 값 반환 