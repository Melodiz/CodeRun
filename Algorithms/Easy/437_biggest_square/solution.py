# Solution for https://coderun.yandex.ru/problem/biggest-square/

def solution():
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    
    # base
    for i in range(n):
        dp[i][0] = data[i][0]
    for j in range(m):
        dp[0][j] = data[0][j]
    
    # fill dp table
    for i in range(1, n):
        for j in range(1, m):
            if data[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    max_value = 0
    ans_i, ans_j = 0, 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] > max_value:
                max_value = dp[i][j]
                ans_i, ans_j = i, j
    print(max_value)
    print(ans_i-max_value+2, ans_j-max_value+2)
    return 0


if __name__ == "__main__":
    solution()
