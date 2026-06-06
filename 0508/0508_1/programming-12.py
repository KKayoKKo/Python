text = input("문자열을 입력하시오: ")
bad_words = input("금지할 글자를 입력하시오: ").split()

for w in bad_words:
    star = ""
    for i in w:
        star = star + "*"
    text = text.replace(w, star)

print(text)

#361p 12번 문제