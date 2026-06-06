schedule = {}

for i in range(2):
    d = input("날짜를 입력하시오: ")
    s = input("일정을 입력하시오: ")

    if d not in schedule:
        schedule[d] = []

    schedule[d].append(s)
    
#360p 7번 문제