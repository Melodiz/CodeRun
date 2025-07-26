def solution(n: int, a: list[int]) -> int:
    left, right = 0, 0
    max_length = 0
    window_elements = dict()
    while right < n:
        if a[right] in window_elements.keys() or len(window_elements.keys()) < 2:
            window_elements[a[right]] = window_elements.get(a[right], 0) + 1
            right += 1
            max_length = max(max_length, right - left) if len(window_elements.keys()) == 2 else max_length
        else:
            window_elements[a[left]] -= 1
            if window_elements[a[left]] == 0:
                del window_elements[a[left]]
            left += 1
    return max_length


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))