def read_input():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return n, m, matrix 


def solve(matrix, n, m):
    dp = [[0] * m for _ in range(n)]
    history = [[''] * m for _ in range(n)]
    
    # Initialize first row
    dp[0][0] = matrix[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        history[0][j] = 'R'
    
    # Initialize first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        history[i][0] = 'D'

    # Fill the rest of dp and history
    for i in range(1, n):
        for j in range(1, m):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
                history[i][j] = 'D'
            else:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
                history[i][j] = 'R'

    # Backtrack to find the path
    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        path.append(history[i][j])
        if history[i][j] == 'D':
            i -= 1
        else:
            j -= 1
    
    return dp[-1][-1], ''.join(reversed(path))

def main():
    n, m, matrix = read_input()
    value, path = solve(matrix, n, m)
    print(value)
    print(' '.join(path))

if __name__ == "__main__":
    main()