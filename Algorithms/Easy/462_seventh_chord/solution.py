# Solution for https://coderun.yandex.ru/problem/seventh-chord
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    res = 0
    for k in range(1, n+1):
        if a[k-1] >= k*k:
            res = k
        else:
            break
    print(res)

if __name__ == "__main__":
    main()
