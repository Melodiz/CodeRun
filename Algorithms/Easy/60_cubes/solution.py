# Solution for https://coderun.yandex.ru/problem/cubes/

def solution():
    n, m = map(int, input().split())
    A, B = set([int(input()) for _ in range(n)]), set([int(input()) for _ in range(m)])
    intersect = A.intersection(B)
    print(len(intersect))
    print(*sorted(intersect))
    print(len(A-intersect))
    print(*sorted(A-intersect))
    print(len(B-intersect))
    print(*sorted(B-intersect))

if __name__ == "__main__":
    solution()
