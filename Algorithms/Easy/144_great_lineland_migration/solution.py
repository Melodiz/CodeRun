# Solution for https://coderun.yandex.ru/problem/great-lineland-migration/
# import stack with O(1) push and pop operations
from collections import deque

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    stack = deque()
    ans = [-1] * n
    for i, val in enumerate(arr):
        if not stack or arr[stack[-1]] <= val:
            stack.append(i)
            continue
        else:
            while stack and arr[stack[-1]] > val:
                ans[stack.pop()] = i
            stack.append(i)
    print(*ans)

if __name__ == "__main__":
    main()