# Solution for https://coderun.yandex.ru/problem/matrix-operations
# Other solutions: https://github.com/Melodiz/CodeRun

def matrix_mult(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result

def matrix_transpose(a):
    rows, cols = len(a), len(a[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = a[i][j]

    return result

def main():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    b = []
    for _ in range(m):
        b.append(list(map(int, input().split())))

    c = matrix_mult(a, b)
    d = matrix_transpose(c)

    for row in d:
        print(*row)

if __name__ == "__main__":
    main()
