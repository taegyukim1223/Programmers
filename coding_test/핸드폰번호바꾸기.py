
def solution(phone_number):
    num = len(phone_number) - 4
    answer = num * '*' + phone_number[num : len(phone_number)]

    return answer


# 정규식을 활용해서? 정규표현식은 일단 패스 나중에 제대로 공부해보자

import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)


#약수의 합구하기

def solution(n):
    a = 0
    for i in range(1,n+1):
        if n % i == 0 :
            a += i
    return a

#filter 함수? map과 다르게 함수가 true냐 false냐에 따라 리스트화할지 결정한다.

def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))

#하샤드 수 찾기
def solution(x):
    a = 0
    for i in str(x) :
        i = int(i)
        a += i
    if x % a == 0 :
        return True

    else :
        return False

#콜라츠 추측

def solution(num):
    a = 0

    while a < 500 :
        if num % 2 == 0 :
            num = num/2
            a += 1
        elif num % 2 == 1 and num != 1:
            num = (num * 3) + 1
            a += 1
        elif num == 1 :
            break

    if a == 500 :
        return -1
    else :
        return a

#정수 제곱근 판별

def solution(n):
    import math
   
    n = math.sqrt(n)
    
    
    if n.is_integer():
        return (n+1) ** 2
    
    else :
        return -1

# 제곱근을 접근을 이렇게 했다고? n ** (1/2)

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'

# 제곱근 판단을 sqrt해준뒤 % 1로 알아낸다??

def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2