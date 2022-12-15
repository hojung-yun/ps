# 동적계획법
def solution(n):
    if n % 2:
        return 0
    dp = [1, 3, 11]
    for i in range(n // 2 - 2):
        answer = 3 * dp[i + 2]
        for j in range(i + 2):
            answer += 2 * dp[j]
        dp.append(answer % 1000000007)
    
    return dp[n // 2]