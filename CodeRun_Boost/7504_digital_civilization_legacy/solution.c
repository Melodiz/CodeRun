#include <stdbool.h>

bool check(long long k_ll, long long n_ll, long long m_ll) {
    if (k_ll == 1) {
        return (n_ll + 1) >= m_ll;
    }

    __int128_t k = k_ll;
    __int128_t n = n_ll;
    __int128_t m = m_ll;

    __int128_t side_sum = 1; 
    __int128_t c = 1;        

    long long limit = n_ll / 2;

    for (long long j = 1; j <= limit + 1; ++j) {
        __int128_t c_next = c * (n - j + 1) / j;

        if (c_next >= k) {
            __int128_t middle_len = n - 2 * j + 1;
            __int128_t total_supported = side_sum * 2 + k * middle_len;
            return total_supported >= m;
        }
        
        side_sum += c_next;
        c = c_next;
    }

    return true;
}


long long solution(long long n, long long m) {
    long long low = 1;
    long long high = m;
    long long ans = m;

    while (low <= high) {
        long long k = low + (high - low) / 2;
        if (k == 0) {
            low = 1;
            continue;
        }

        if (check(k, n, m)) {
            ans = k;
            high = k - 1;
        } else {
            low = k + 1;
        }
    }

    return ans;
}