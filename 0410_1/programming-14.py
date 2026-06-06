def test_sqrt(x, g):
    while True:
        print("추측값:", round(g, 4), "x/g:", round(x / g, 4))

        if abs(g - x / g) < 0.0001:
            return g

        g = (g + x / g) / 2

result = test_sqrt(2, 1.0)

print("제곱근 =", result)

# 248p 14번 문제