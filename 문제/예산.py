
def solution(d, budget):
    cnt = 0
    d = sorted(d)
    for i in d :
        budget = budget - i
        cnt += 1
        if budget < 0 :
            cnt -= 1
            break
    return cnt

    
#.pop()는 맨 마지막 항목을 삭제합니다!! 그것을 이용한 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)