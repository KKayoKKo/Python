def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = int(input("점수를 입력하세요: "))

print("성적은", getGrade(score), "입니다.")

# 성적이 90점이라면 A, 80점 이상이라면 B, 70점 이상이라면, C 60점 이상이면 D, 그외에는 F를 반환하는 함수 p246
