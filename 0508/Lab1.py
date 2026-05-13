s1 = input("첫 번째 문자열:")
s2 = input("두 번째 문자열:")

list1 = list(set(s1) & set(s2))   # & 는 교집합 연산자 -> 교집합 결과는 set 형태이므로 리스트로 바꿈
print("\n공통적인 글자:", end=" ")

for i in list1:
    print(i, end=" ")
    

# 문자열의 공통 문자 Lab