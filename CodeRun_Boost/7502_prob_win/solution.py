def solve(a: int, k: int, n: int) -> int:
    MOD = 10**9 + 7

    def power(base, exp):
        res = 1
        base %= MOD
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % MOD
            base = (base * base) % MOD
            exp //= 2
        return res

    def mod_inverse(n):
        return power(n, MOD - 2)

    small_val = min(k, n)
    large_val = max(k, n)

    if small_val == 0:
        return 1

    numerator = 1
    for i in range(1, small_val + 1):
        numerator = (numerator * i) % MOD

    denominator = 1
    for i in range(1, small_val + 1):
        denominator = (denominator * (large_val + i)) % MOD
    
    return (numerator * mod_inverse(denominator)) % MOD