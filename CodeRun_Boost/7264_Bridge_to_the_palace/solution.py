def solution(n, a):
    a.sort()
    left = 0
    max_keep = 0

    for right in range(n):
        while a[right] - a[left] >= n:
            left += 1

        current_keep = right - left + 1
        if current_keep > max_keep:
            max_keep = current_keep

    min_moves = n - max_keep
    return min_moves


