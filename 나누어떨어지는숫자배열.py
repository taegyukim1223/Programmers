def solution(arr, divisor):
    a = []
    for i in arr :
        if i % divisor == 0 :
            a.append(i)
        else :
            continue
            
    if a == [] :
        return [-1]
   
    return sorted(a)