#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

long long solution(int n) {
    if (n < 5) {
        return 0;
    }

    bool* is_prime = (bool*)malloc((n + 1) * sizeof(bool));
    for (int i = 0; i <= n; i++) {
        is_prime[i] = true;
    }
    is_prime[0] = is_prime[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                is_prime[i] = false;
            }
        }
    }

    long long count1_mod4 = 0;
    long long count3_mod4 = 0;

    for (int p = 3; p <= n; p++) {
        if (is_prime[p]) {
            if (p % 4 == 1) {
                count1_mod4++;
            } else if (p % 4 == 3) {
                count3_mod4++;
            }
        }
    }

    free(is_prime);

    return count1_mod4 * count3_mod4;
}