def check(n, m, k):
    return k**2 <= n+m and k**2//2 <= min(n, m)


def solution(n, m):
    left, right = 0, 150000
    while left <= right:
        mid = (left + right) // 2
        if check(n, m, mid):
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution(n, m))