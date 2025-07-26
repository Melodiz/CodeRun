def solution(n, q, a, queries):
    diff = [0] * (n + 1)

    for l, r in queries:
        diff[l - 1] += 1
        diff[r] -= 1

    freq = [0] * n
    current_freq = 0
    for i in range(n):
        current_freq += diff[i]
        freq[i] = current_freq

    a.sort(reverse=True)
    freq.sort(reverse=True)

    ans = 0
    for i in range(n):
        ans += a[i] * freq[i]

    return ans