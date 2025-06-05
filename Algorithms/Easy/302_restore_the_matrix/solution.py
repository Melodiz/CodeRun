# Solution for https://coderun.yandex.ru/problem/restore-the-matrix
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    closed = set()
    for row in matrix:
        closed.update(set(row))
    cur = 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                while cur in closed:
                    cur += 1
                matrix[i][j] = cur
                cur += 1
    for row in matrix:
        print(*row)

if __name__ == "__main__":
    main()
