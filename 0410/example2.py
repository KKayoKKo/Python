def add(*numbers) : # numbers → 여러 개의 값을 한 번에 받는 매개변수
        sum = 0
        for n in numbers:
                sum = sum + n
        return sum
    
print(add(10, 20)) # 10 + 20 = 30
print(add(10, 20, 30)) # 10 + 20 + 30 = 60

# 여러 개의 숫자를 입력받아서 모두 더해주는 것.