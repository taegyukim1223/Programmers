
# 정수 내림차순정리
def solution(n):
    n = int(''.join(sorted(str(n), reverse = True))
    return n

2
#문자열 내림차순정리

def solution(s):
    return ''.join([chr(n) for n in sorted([ord(c) for c in list(s)], reverse=True)])

#chr() 와 ord()란? 아스키코드로 반환해주는것, chr(아스키코드), ord(문자숫자)

#힙메모리와 스택메모리란? 힙메모리는 스택메모리의 단점을 보완하기 위해 나옴
#스택 메모리는 용량한계와 메모리의 수명이 낮음.힙메모리는 둘다 가변적, 단점 느림