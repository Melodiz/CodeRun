# Solution for https://coderun.yandex.ru/problem/rectangle-sum
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # Build prefix sum matrix (1-based indexing for easier calculations)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = matrix[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        res = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
        print(res)

if __name__ == "__main__":
    main()
