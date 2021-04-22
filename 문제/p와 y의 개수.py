def solution(s):
    s.lower()
    p_num = 0
    y_num = 0
    
    for i in s :
        if i == 'p' :
            p_num += 1
        elif i == 'y' :
            y_num += 1
            
    if p_num == y_num and p_num != 0 and y_num != 0 :
        return True
        
    elif p_num == 0 and y_num == 0 : 
        return True
    
    else : 
        return False