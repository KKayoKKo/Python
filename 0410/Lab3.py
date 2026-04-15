def f(x):
    return(x**2-x-1) # 이 함수의 근(=0이 되는 x)을 찾는 게 목표

def bisection_method(a, b, error):
    if f(a)*f(b) > 0: # f(a)와 f(b)의 부호가 같으면
        print("구간에서 근을 찾을 수 없습니다.")
    else:    
        while (b - a)/2.0 > error: # 구간 길이가 오차보다 클 때 계속 반복
            midpoint = (a + b)/2.0 # 중점을 계산한다.
        if f(midpoint) == 0: # 중점이 정확히 근이면 바로 반환
            return(midpoint)
        elif f(a)*f(midpoint) < 0: # 근이 a ~ midpoint 사이에 있음
            b = midpoint
        else: # 근이 midpoint ~ b 사이에 있음
            a = midpoint
            
            
    return(midpoint)
answer = bisection_method(1, 2, 0.0001) # 구간 [1, 2]에서 근 찾기

print("x**2-x-1의 근:", answer)

# 이분법 랩 
# 구간을 계속 반으로 나누면서 근이 있는 쪽만 남겨서 점점 정확한 값을 찾는 알고리즘