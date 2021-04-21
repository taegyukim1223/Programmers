
def solution(arr):
    arr.remove(min(arr))
    if arr == [] :
        return [-1]
    else :
        return arr


#리스트 원소제거 list.remove(원소), del list[index] 인덱스에 해당하는 원소 삭제
#리스트 원소주입 list.insert(index, 원소)
# list.index(x) x값이 리스트에 있으면 인덱스을 리턴해준다. del과 함께 사용하면 del list[list.index(x)]
# pop란? pop(index) 인덱스에 해당하는 값을 지우고 값을 반환
