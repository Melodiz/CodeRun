def solution(n: int, m: int) -> int:

    def check(k: int, n: int, m: int) -> bool:
        if k == 1:
            return n + 1 >= m

        side_sum = 1
        c = 1
        
        limit = (n // 2) + 1
        
        for j in range(1, limit + 1):
            c_next = c * (n - j + 1) // j
            
            if c_next >= k:
                middle_len = n - 2 * j + 1
                total_supported = side_sum * 2 + k * middle_len
                return total_supported >= m
            
            side_sum += c_next
            c = c_next

        return True

    low = 1
    high = m
    ans = m

    while low <= high:
        k = (low + high) // 2
        if k == 0:
            low = 1
            continue
        
        if check(k, n, m):
            ans = k
            high = k - 1
        else:
            low = k + 1
            
    return ans