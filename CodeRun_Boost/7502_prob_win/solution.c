#include <stdio.h>

long long power(long long base, long long exp) {
    long long res = 1;
    long long MOD = 1e9 + 7;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) {
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inverse(long long n) {
    long long MOD = 1e9 + 7;
    return power(n, MOD - 2);
}

long long solve(int a, int k, int n) {
    long long MOD = 1e9 + 7;

    if (k == 0 || n == 0) {
        return 1;
    }

    long long small_val = (k < n) ? k : n;
    long long large_val = (k > n) ? k : n;

    long long numerator = 1;
    for (long long i = 1; i <= small_val; ++i) {
        numerator = (numerator * i) % MOD;
    }

    long long denominator = 1;
    for (long long i = 1; i <= small_val; ++i) {
        denominator = (denominator * (large_val + i)) % MOD;
    }
    
    return (numerator * mod_inverse(denominator)) % MOD;
}