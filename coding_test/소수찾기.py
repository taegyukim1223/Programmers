def solution(n):
    a =[]
    for i in range(2,n+1) :
        cnt = 0
        for l in range(2, i+1):
            if i % l == 0:
                cnt += 1
        if cnt == 1:
            a.append(i)
        
    return len(a)

n = 9999
def solution(n):
    # 리스트 컴프리헨션
    a = [ i for i in range( 10, n+1 ) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 ] 
    b = len(a) + 4 
    return b
solution(n)

