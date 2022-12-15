# 동적계획법
def solution(board):
    r, c = len(board), len(board[0])
    answer = 0 # 표에서 1로 이루어진 가장 큰 정사각형의 한 변의 길이
    for y in range(r):
        for x in range(c):
            if y >= 1 and x >= 1 and board[y][x]:
                board[y][x] = min(min(board[y-1][x-1], board[y-1][x]), board[y][x-1]) + 1 # y행 x열에 위치한 칸을 오른쪽 하단 모서리로 갖는 정사각형의 최대 길이
            answer = max(answer, board[y][x])
    
    return answer ** 2