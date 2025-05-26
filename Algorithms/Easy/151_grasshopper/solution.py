# Solution for https://coderun.yandex.ru/problem/grasshopper/
from functools import lru_cache

@lru_cache(None)
def rec(cur, goal, k):
    if cur == goal: return 1
    if cur > goal: return 0
    return sum(rec(cur + i, goal, k) for i in range(1, k + 1))


def solution():
    n, k = map(int, input().split())
    print(rec(1, n, k))

if __name__ == "__main__":
    solution()
