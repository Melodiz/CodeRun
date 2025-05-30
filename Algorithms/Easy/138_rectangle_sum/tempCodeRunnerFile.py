# Solution for https://coderun.yandex.ru/problem/rectangle-sum
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n, m, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(sum(matrix[i][j] for i in range(x1-1, x2) for j in range(y1-1, y2)))

if __name__ == "__main__":
    main()
