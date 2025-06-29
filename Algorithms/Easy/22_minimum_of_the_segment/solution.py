# Solution for https://coderun.yandex.ru/problem/minimum-of-the-segment
# Other solutions: https://github.com/Melodiz/CodeRun
from collections import deque

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    deq = deque()
    for i in range(k):
        while deq and a[deq[-1]] >= a[i]:
            deq.pop() 
        deq.append(i)
    ans = []
    print(a[deq[0]])
    for i in range(k, len(a)):
        while deq and a[deq[-1]] >= a[i]:
            deq.pop() 
        while deq and deq[0] <= i - k:
            deq.popleft()
        deq.append(i)
        print(a[deq[0]])
    return 


if __name__ == '__main__':
    main()
