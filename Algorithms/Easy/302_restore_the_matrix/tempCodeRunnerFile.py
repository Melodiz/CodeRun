# Solution for https://coderun.yandex.ru/problem/restore-the-matrix
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            v = matrix[i][j]
            if v != 0:
                flat_i, flat_j = (v - 1) // n, (v - 1) % n
                if (i, j) != (flat_i, flat_j):
                    ans[i][j], ans[flat_i][flat_j] = ans[flat_i][flat_j], ans[i][j]
    for row in ans:
        print(*row)

if __name__ == "__main__":
    main()
