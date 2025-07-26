def solution(n: int, m: int, p: list[int]) -> list[int]:
    ans = [0] * n
    if p[0] == -1:
        p[0] = m
    ans[0] = p[0]
    for i in range(1,n):
        if p[i] == -1: p[i] = p[i-1]+m
        if p[i] < p[i-1]+m: return [-1]
        ans[i] = p[i] - p[i-1] if i > 0 else p[i]
    return ans