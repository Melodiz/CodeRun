import sys

def calculate_mex_from_range(a: list[int], start: int, end: int) -> int:
    if start > end:
        return 0
    
    length = end - start + 1
    seen = [False] * (length + 1)
    for i in range(start, end + 1):
        val = a[i]
        if 0 <= val < len(seen):
            seen[val] = True
            
    mex = 0
    while mex < len(seen) and seen[mex]:
        mex += 1
    return mex

def check(V: int, n: int, a: list[int]) -> bool:
    l0, r0 = -1, -1
    for i in range(n):
        if a[i] > V:
            if l0 == -1:
                l0 = i
            r0 = i
            
    if l0 == -1:  # Case 1: All elements in `a` are <= V.
        has_non_zero = False
        for x in a:
            if x != 0:
                has_non_zero = True
                break
        
        if has_non_zero:
            return True
        else:
            return V >= 1
    else:  # Case 2: Some elements in `a` are > V.
        m = calculate_mex_from_range(a, l0, r0)
        return m <= V

def calculate_answer(n: int, a: list[int]) -> list[int]:
    if n == 1:
        m = 1 if a[0] == 0 else 0
        return [m, m, m, m]

    mex_a = calculate_mex_from_range(a, 0, n - 1)
    max_a = max(a) if a else 0

    # --- 1. minMax (with corrected check function) ---
    low, high = 0, n
    minMax = n
    while low <= high:
        mid = (low + high) // 2
        if check(mid, n, a):
            minMax = mid
            high = mid - 1
        else:
            low = mid + 1
            
    # --- 2. maxMax ---
    maxMax = max(max_a, mex_a)
    
    # --- 3. minMin ---
    minMin = 0
    
    # --- 4. maxMin ---
    maxMin = mex_a
    
    return [minMax, maxMax, minMin, maxMin]

class FastInput:
    def __init__(self):
        pass

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_line().split())

def solution():
    fast_input = FastInput()
    try:
        t = fast_input.read_int()
        answers = []
        for _ in range(t):
            n = fast_input.read_int()
            a = list(fast_input.read_ints())
            test_answers = calculate_answer(n, a)
            answers.append(' '.join(map(str, test_answers)))
        print('\n'.join(answers))
    except (IOError, ValueError):
        pass

solution()