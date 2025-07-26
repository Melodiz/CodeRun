from functools import lru_cache

@lru_cache(maxsize=None)
def rec(current_n: int) -> int:
    MOD = 10**9 - 7538
    if current_n == 0:
        return 1
    
    term1 = pow(rec(current_n // 2), rec(current_n // 3), MOD)
    term2 = (5 * rec(current_n // 4)) % MOD
    term3 = current_n % MOD

    return (term1 + term2 + term3) % MOD

def solution(n: int) -> int:
    return rec(n)