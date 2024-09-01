def min_cost(grid, n, m):
    # greedy approach to solve the problem
    # minimize the cost of moving from top-left to bottom-right
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[n-1][m-1]


def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_cost(grid, n, m))


if __name__ == "__main__":
    main()
