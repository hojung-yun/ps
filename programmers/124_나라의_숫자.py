def solution(n):
    table = ['1', '2', '4']
    answer = ''
    while n:
        n -= 1
        answer = table[n % 3] + answer
        n //= 3
    
    return answer