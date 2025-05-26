# Solution for https://coderun.yandex.ru/problem/a-1-find-most-frequent/
from collections import Counter

def solution():
    n = int(input())
    arr = Counter(map(int, input().split()))
    max_freq = max(arr.values())
    return max(key for key, value in arr.items() if value == max_freq)

if __name__ == "__main__":
    print(solution())
