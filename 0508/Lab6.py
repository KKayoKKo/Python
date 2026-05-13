text_data = "Create the highest, grandest vision possible for your life, because you become what you believe"

word_dic = {}  # 단어와 출현 횟수를 저장하는 딕셔너리

for w in text_data.split(): # 텍스트를 단어로 분리해서 반복함

    if w in word_dic: # 이미 나온 단어면 +1
        word_dic[w] += 1
 
    else: #  # 처음 나온 단어면 1로 초기화함
        word_dic[w] = 1

for w, count in sorted(word_dic.items()): #  알파벳 순으로 정렬해서 출력함
    print(w, "의 등장횟수=", count)


from collections import Counter

text_data = "Create the highest, grandest vision possible for your life, because you become what you believe"

a = Counter(text_data.split())
print(a)

# 단어 카운터 만들기 Lab 