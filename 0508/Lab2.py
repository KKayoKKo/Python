txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words) # 리스트를 집합(set)으로 변환 -> set은 중복 데이터를 자동으로 제거

print("사용된 단어의 개수= ", len(unique)) # 중복 제거 후 남은 단어 개수를 출력
print(unique)