quiz = {"파이썬": "최근에 가장 떠오르는 프로그래밍 언어"}

for answer in quiz:
    print("다음은 어떤 단어에 대한 설명일까요?")
    print('"', quiz[answer], '"')
    print("(1)파이썬 (2)변수 (3)함수 (4)리스트")

    user = input()

    if user == answer:
        print("정답입니다!")
    else:
        print("틀렸습니다.")
        
#361p 11번 문제