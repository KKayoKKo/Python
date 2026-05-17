class Student:
        def __init__(self, name=None, age=0): # 이름과 나이 저장
                self.__name = name # __ 붙으면 외부에서 직접 접근 금지
                self.__age = age  # __ 붙으면 외부에서 직접 접근 금지


obj = Student()
print(obj.__age)

# __ 를 붙이면 클래스 내부에서만 사용하는 private(비공개) 변수처럼 동작한다.
# 정보 은닉