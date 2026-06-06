def deci2bin(n):
    result = ""

    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    return result

num = int(input("10진수: "))
print(deci2bin(num))
      
# 10진수를 2진수로 변환하는 함수 deci2bin(n)을 작성 p248