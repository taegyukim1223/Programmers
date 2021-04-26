def solution(x, n):
    answer = []
    for i in range(1, n+1):
         answer.append(x*i)
    return answer


# 리스트 컴프리헨션에 연산기호 가능하다니!
    def number_generator(x, n):
    return [x*(i+1) for i in range(n)]