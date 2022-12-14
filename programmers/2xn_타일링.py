def solution(n):
    # n이 1인 경우
    if n == 1:
        return 1
    # n이 2인 경우
    if n == 2:
        return 2
    # n이 3이상인 경우    
    x = 3
    back_2, back_1 = 1, 2 # 각각 가로의 길이가 x-2, x-1 일 때, 직사각형을 채우는 방법의 수
    answer = 0
    while x <= n:
        answer = (back_2 + back_1) % 1000000007 # 
        x += 1
        back_2 = back_1
        back_1 = answer
    
    return answer