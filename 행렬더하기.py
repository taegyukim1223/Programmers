def solution(arr1, arr2):
    cnt = 0
    
    arr4 = []
    for i in range(len(arr1)) :
        for l in range(len(arr2)) :
            arr3 =[]
            b = arr1[i][l] + arr2[i][l]
            arr3.append(b)
        arr4.append(arr3)
        
    return arr4