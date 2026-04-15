def myfunc(**kwargs): # **kwargs → 키=값 형태의 여러 개 인자를 딕셔너리로 받음
        result = ""
        for arg in kwargs.values(): # 딕셔너리의 값들만 하나씩 꺼내서 반복
                    result += arg
        return result
    
print(myfunc(a="Hi!", b="Mr.", c="Kim"))


# 키워드 인자로 받은 문자열들을 모두 이어붙여서 반환함.