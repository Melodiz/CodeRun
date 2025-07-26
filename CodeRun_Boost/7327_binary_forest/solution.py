def solve(n: int, a: list[int], m: int, b: list[int]) -> int:
    zeros_a = [i for i, val in enumerate(a) if val == 0]
    zeros_b = [i for i, val in enumerate(b) if val == 0]

    suffix_ones_a = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_ones_a[i] = suffix_ones_a[i + 1] + a[i]

    suffix_ones_b = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        suffix_ones_b[i] = suffix_ones_b[i + 1] + b[i]

    max_len = 0

    max_len = min(suffix_ones_a[0], suffix_ones_b[0])

    max_k = min(len(zeros_a), len(zeros_b))
    for k in range(1, max_k + 1):
        idx_a = zeros_a[k - 1]
        idx_b = zeros_b[k - 1]

        ones_in_suffix_a = suffix_ones_a[idx_a + 1]
        ones_in_suffix_b = suffix_ones_b[idx_b + 1]

        current_len = k + min(ones_in_suffix_a, ones_in_suffix_b)
        
        if current_len > max_len:
            max_len = current_len

    return max_len