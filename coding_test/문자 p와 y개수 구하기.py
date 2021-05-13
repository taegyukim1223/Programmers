
def solution(s):
    pNum = 0
    yNum = 0
    for i in s.lower():
        if i == 'p':
            pNum += 1
        elif i == 'y':
            yNum += 1
    if pNum == yNum:
        return True
    return False


# count() 함수사용
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')