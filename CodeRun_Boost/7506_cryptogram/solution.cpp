#include <bits/stdc++.h>

long long calculate_answer(int n, int k, std::vector<int>& a) {
    std::vector<int> counts(n + 1, 0);
    for (int val : a) {
        counts[val]++;
    }

    int M = n / k;
    if (M == 0) {
        return 0; // If n < k, no value can be a multiple of k (since a_i <= n).
    }
    std::vector<int> f(M + 1, 0);
    for (int i = k; i <= n; i += k) {
        if (counts[i] > 0) {
            f[i / k] = counts[i];
        }
    }

    std::vector<long long> num_multiples(M + 1, 0);
    for (int d = 1; d <= M; ++d) {
        for (int j = d; j <= M; j += d) {
            num_multiples[d] += f[j];
        }
    }

    std::vector<long long> pairs_with_gcd(M + 1, 0);
    for (int d = M; d >= 1; --d) {
        if (num_multiples[d] < 2) {
            continue; // Cannot form a pair.
        }
        
        long long total_pairs_multiple_of_d = num_multiples[d] * (num_multiples[d] - 1) / 2;
        

        for (int j = 2 * d; j <= M; j += d) {
            total_pairs_multiple_of_d -= pairs_with_gcd[j];
        }
        
        pairs_with_gcd[d] = total_pairs_multiple_of_d;
    }

    return pairs_with_gcd[1];
}

// Provided I/O handling function.
void solve() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;

    for (int test = 0; test < t; ++test) {
        int n, k;
        std::cin >> n >> k;

        std::vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> a[i];
        }

        long long answer = calculate_answer(n, k, a);
        std::cout << answer << '\n';
    }   
}