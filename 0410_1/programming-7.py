def getIntRange(a, b, msg):
    while True:
        num = int(input(msg))

        if num >= a and num <= b:
            return num

month = getIntRange(1, 12, "월을 입력하시오(1부터 12사이의 값): ")
day = getIntRange(1, 31, "일을 입력하시오(1부터 31사이의 값): ")

print(month, "월", day, "일")

# 사용자가 일정 구간의 값을 입력할 때까지 사용자에게 입력을 요청하는 함수 getlntRange(a, b, msg)를 작성하고 테스트 p247