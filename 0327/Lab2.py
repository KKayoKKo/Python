COUNT = 100 # 구간을 몇 개로 나눌지 정하는 값
START = 1.0 # 구간의 시작점
END = 2.0 # 구간의 끝점

for i in range(COUNT):
    x = START + i*((END-START)/COUNT)
    f = (x**2-x -1)
    if abs(f-0.0) < 0.01:
print("방정식의 해는", x)

# f(x) = x^2−x−1 해를 찾는 코드
# 방정식의 해 구하기 랩 예제