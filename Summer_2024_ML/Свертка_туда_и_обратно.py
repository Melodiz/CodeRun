import sys
from numpy.linalg import solve


def Convolution2D(A, B, n, m, k):
    C = [[0] * (m - k + 1) for _ in range(n - k + 1)]
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            for l in range(k):
                for p in range(k):
                    C[i][j] += A[i + l][j + p] * B[l][p]
    return C


def RevertConvolution2D(A, C, n, m, k):
    X = buildX(A, n, m, k)
    Y = BuildY(C, n, m, k)
    B = solve(X, Y).round().astype(int)
    return [list(B[i * k:(i + 1) * k]) for i in range(k)]


def buildX(A, n, m, k):
    X = []
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            row = []
            for l in range(k):
                for p in range(k):
                    row.append(A[i + l][j + p])
            X.append(row)
            if len(X) == k**2:
                return X


def BuildY(C, n, m, k):
    Y = []
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            Y.append(C[i][j])
            if len(Y) == k**2:
                return Y

def main():
    n, m, k = map(int, input().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    C = [list(map(int, sys.stdin.readline().split())) for _ in range(n - k + 1)]
    result = RevertConvolution2D(A, C, n, m, k)
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()