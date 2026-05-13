phrase = input("문자열을 입력하시오: ")
acronym = ""

for word in phrase.upper().split(): # 입력된 문자열을 대문자로 바꾼 후 단어로 분리해서 반복함
    acronym += word[0]  

print(acronym)