def solution(n, m):
    min_num = min(n, m)
    max_num = max(n, m)
    a = min_num    

    #최대공약수 뽑아내기
    while min_num % a != 0 or max_num % a != 0 :
        a = a - 1

    s = a

    b = max_num  

    # 최소공배수 뽑아내기
    while b % min_num != 0 :
        b = b + max_num 

    k = b

    return [s, k]


    