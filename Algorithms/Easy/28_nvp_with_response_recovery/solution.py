# Solution for https://coderun.yandex.ru/problem/nvp-with-response-recovery
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in dp
    max_len = max(dp)
    idx = dp.index(max_len)

    # Recover the sequence
    lis = []
    while idx != -1:
        lis.append(arr[idx])
        idx = prev[idx]
    lis.reverse()

    print(' '.join(map(str, lis)))

if __name__ == "__main__":
    main()
