#include <stdio.h>
#include <stdlib.h>

void solution();

long long calculate_answer(int n, int k, int* a) {
    int* counts = (int*)calloc(n + 1, sizeof(int));
    if (!counts) return -1; // Memory allocation check

    for (int i = 0; i < n; i++) {
        counts[a[i]]++;
    }

    int M = n / k;
    if (M == 0) {
        free(counts);
        return 0;
    }
    int* f = (int*)calloc(M + 1, sizeof(int));
    if (!f) { free(counts); return -1; }

    for (int i = k; i <= n; i += k) {
        if (counts[i] > 0) {
            f[i / k] = counts[i];
        }
    }
    free(counts);

    long long* num_multiples = (long long*)calloc(M + 1, sizeof(long long));
    if (!num_multiples) { free(f); return -1; }
    
    for (int d = 1; d <= M; d++) {
        for (int j = d; j <= M; j += d) {
            num_multiples[d] += f[j];
        }
    }

    free(f);

    long long* pairs_with_gcd = (long long*)calloc(M + 1, sizeof(long long));
    if (!pairs_with_gcd) { free(num_multiples); return -1; }

    for (int d = M; d >= 1; d--) {
        if (num_multiples[d] < 2) {
            continue;
        }
        
        long long total_pairs_multiple_of_d = num_multiples[d] * (num_multiples[d] - 1) / 2;
        
        for (int j = 2 * d; j <= M; j += d) {
            total_pairs_multiple_of_d -= pairs_with_gcd[j];
        }
        
        pairs_with_gcd[d] = total_pairs_multiple_of_d;
    }
    free(num_multiples);
    
    long long result = pairs_with_gcd[1];
    
    free(pairs_with_gcd);

    return result;
}

// ввод/вывод
// не изменяйте сигнатуру метода
void solution() {
    int t;
    scanf("%d", &t);

    for (int test = 0; test < t; ++test) {
        int n, k;
        scanf("%d %d", &n, &k);

        int* a = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
        }

        long long answer = calculate_answer(n, k, a);

        printf("%lld\n", answer);

        // Освобождение памяти
        free(a);
    }
}