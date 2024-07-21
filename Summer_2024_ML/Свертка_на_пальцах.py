import sys


def Convolution2D(A, B, n, m, k):
    C = [[0] * (m - k + 1) for _ in range(n - k + 1)]
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            for l in range(k):
                for p in range(k):
                    C[i][j] += A[i + l][j + p] * B[l][p]
    return C


def main():
    n, m = map(int, input().split())
    # read the matrix n x n
    A = []
    for _ in range(n):
        A.append(list(map(int, sys.stdin.readline().split())))
    k = int(input())
    B = []
    for _ in range(k):
        B.append(list(map(int, sys.stdin.readline().split())))
    result = Convolution2D(A, B, n, m, k)
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()
