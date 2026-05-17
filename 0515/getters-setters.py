class Student:
    def __init__(self, name=None, age=0):
        self.__name = name # __name -> private 변수
        self.__age = age # # __age -> private 변수

    def getAge(self): # 접근자 (getter) -> 값을 가져오는 함수 (객체 안의 값을 읽기 위해 사용)
        return self.__age 

    def getName(self):
        return self.__name 

    def setAge(self, age): # 설정자 (setter) -> 값을 설정하는 함수 (객체 내부 값을 수정할 때 사용)
        self.__age = age 

    def setName(self, name):
        self.__name = name 


obj = Student("Hong", 20)
obj.getName() 

# 인스턴스 변수값을 반환하는 접근자(getters)
# 인스턴스 변수값을 설정하는 설정자(setters)
# 접근자와 설정자