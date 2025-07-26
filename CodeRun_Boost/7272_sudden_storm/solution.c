#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long* solve(int n, int t, long long* a, long long* b) {
    long long total_initial = 0;
    for (int i = 0; i < n; i++) {
        total_initial += a[i];
    }

    long long* res = (long long*)malloc(sizeof(long long) * (t + 1));
    if (res == NULL) {
        return NULL;
    }

    if (t == 0) {
        res[0] = total_initial;
        return res;
    }

    long long* base_diff = (long long*)calloc(t + 3, sizeof(long long));
    long long* adj = (long long*)calloc(t + 3, sizeof(long long));
    if (base_diff == NULL || adj == NULL) {
        free(res);
        free(base_diff);
        free(adj);
        return NULL;
    }

    for (int i = 0; i < n; i++) {
        long long a_i = a[i];
        long long b_i = b[i];

        if (b_i == 0 || a_i == 0) {
            continue;
        }

        long long k_i = (a_i + b_i - 1) / b_i;
        
        long long end = k_i;
        if (end > t) {
            end = t;
        }

        base_diff[1] += b_i;
        
        if (end + 1 < (t + 3)) { // Ensure index is valid for base_diff
            base_diff[end + 1] -= b_i;
        }
            
        if (k_i <= t) {
            long long remainder = a_i - b_i * (k_i - 1);
            if (k_i < t + 3) { // Ensure index is valid for adj
                adj[k_i] += (remainder - b_i);
            }
        }
    }

    res[0] = total_initial;
    long long current_base = 0;
    long long cumulative_loss = 0;
    
    for (int j = 1; j <= t; j++) {
        current_base += base_diff[j]; // j will always be < t+3 here
        long long loss_this_minute = current_base + adj[j]; // j will always be < t+3 here
        cumulative_loss += loss_this_minute;
        res[j] = total_initial - cumulative_loss;
    }

    free(base_diff);
    free(adj);

    return res;
}