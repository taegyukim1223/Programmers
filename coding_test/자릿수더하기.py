# 재귀함수 이용한 자릿수 더하기, 함수정의 안에서 다시 함수를 호출

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

#리스트를 만들때 조건을 걸어서 만들어준 뒤 sum

def sum_digit(number):
    return sum([int(i) for i in str(number)])

# map변수에 리스트말고 string을 줘도 리스트 처럼 취급
def sum_digit(number):
    return sum(map(int,str(number)))

numbers = [2,1,3,4,1]
def solution(numbers):
    a = []
    for i in numbers :
        for l in numbers :
            if numbers.index(i) != numbers.index(l) :
                b = i + l 
                a.append(b)
    
    return list(set(a))
solution(numbers)