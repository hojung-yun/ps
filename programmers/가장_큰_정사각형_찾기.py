def solution(board):
    r, c = len(board), len(board[0])
    answer = min(r, c) # 표에서 1로 이루어진 가장 큰 정사각형의 한 변의 길이
    
    def is_square(y, x, l, board): # 좌측 상단 꼭지점이 y행 x열이고 길이가 l인 정사각형이 board에서 모두 1로 이루어져있는지 여부를 반환하는 함수
        for i in range(l):
            for j in range(l):
                if board[y + i][x + j] != 1:
                    return False
        return True
        
    while answer:
        for y in range(r - answer + 1):
            for x in range(c - answer + 1):
                if is_square(y, x, answer, board):
                    return answer ** 2
        answer -= 1

    return 0

