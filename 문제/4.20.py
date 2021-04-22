#시저암호

def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz' * 2
    alphad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
    new_alpha = ""
    n = n%26
    for i in s :
        if i in alpha:
            num3 = alpha.index(i)
            num1 = num3 + n
            insert_alpha = alpha[num1]
            new_alpha += insert_alpha

        elif i in alphad:
            num3 = alphad.index(i)
            num2 = num3 + n
            insert_alpha = alphad[num2]
            new_alpha += insert_alpha
        
        else :
            new_alpha += i
        
    return new_alpha

# 이상한 문자 만들기

s = "try hello world"
def solution(s):
    i =0 
    newword =""
    for l in s :
        if l != " " and i % 2 == 0 :
            newword += l.upper()
            i += 1
        elif l != " " and i % 2 == 1 :
            newword += l.lower()
            i += 1
        else:
            newword += " "
    
    return newword

solution(s)

# ''.join(list) list요소를 합쳐서 문자로 반환해준다. ''안에 문자를 넣으면 요소사이를 그걸로 채워서 문자열로 만들어준다.
# '구분자'.join(list)

# enumerate() 리스트를 기반으로 인덱스와 요소를 묶어서 반환해준다.

#다른사람 풀이
#def toWeirdCase(s):
# return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])



##자연수 뒤집어 배열로 만들기

def solution(n):
    lista = []
    for i in str(n) :
        i = int(i)
        lista.append(i)
    lista.reverse()
    
    return lista

solution(n)

#def digit_reverse(n):
#    return list(map(int, list(str(n))[::-1])) 

# list[A:B:C]의 의미 LIST를 A부터B까지 C의 가격으로 재배열 C가 음수면 역순으로 재배열



s = "Zbcdefg"
def solution(s):
    return ''.join(list(map(sorted(), list(s)))

solution(s)