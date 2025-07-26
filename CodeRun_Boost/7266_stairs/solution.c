#include <stdlib.h>
#include <limits.h>

int* solution(int n, const int* a) {
    int result_size = n + 1;
    int* result = (int*)calloc(result_size, sizeof(int));
    if (n == 0) {
        free(result);
        return NULL;
    }
     if (n == 1) {
        result[0] = 1;
        result[1] = a[0];
        return result;
    }

    int* dp_plus = (int*)malloc(n * sizeof(int));
    int* dp_minus = (int*)malloc(n * sizeof(int));
    dp_plus[0] = a[0];
    dp_minus[0] = -a[0];

    for (int i = 1; i < n; ++i) {
        int current_plus = a[i];
        int current_minus = -a[i];
        int plus_ok = 0;
        int minus_ok = 0;

        if (dp_plus[i-1] != INT_MAX && dp_plus[i-1] <= current_plus) plus_ok = 1;
        if (dp_minus[i-1] != INT_MAX && dp_minus[i-1] <= current_plus) plus_ok = 1;

        if (dp_plus[i-1] != INT_MAX && dp_plus[i-1] <= current_minus) minus_ok = 1;
        if (dp_minus[i-1] != INT_MAX && dp_minus[i-1] <= current_minus) minus_ok = 1;

        if (!plus_ok && !minus_ok) {
            free(dp_plus);
            free(dp_minus);
            return result;
        }

        if (plus_ok) {
            dp_plus[i] = current_plus;
        } else {
            dp_plus[i] = INT_MAX;
        }

        if (minus_ok) {
            dp_minus[i] = current_minus;
        } else {
            dp_minus[i] = INT_MAX;
        }
    }

    result[0] = 1;
    int current = INT_MAX;

    if (dp_plus[n - 1] != INT_MAX && dp_minus[n - 1] != INT_MAX) {
        current = (dp_plus[n-1] < dp_minus[n-1]) ? dp_plus[n-1] : dp_minus[n-1];
    } else if (dp_plus[n - 1] != INT_MAX) {
        current = dp_plus[n - 1];
    } else {
        current = dp_minus[n - 1];
    }
    result[n] = current;
    
    for (int i = n - 2; i >= 0; --i) {
        int next_val = result[i+2];
        if (dp_plus[i] != INT_MAX && dp_plus[i] <= next_val) {
            if (dp_minus[i] != INT_MAX && dp_minus[i] <= next_val) {
                result[i+1] = (dp_plus[i] < dp_minus[i]) ? dp_plus[i] : dp_minus[i];
            } else {
                result[i+1] = dp_plus[i];
            }
        } else if (dp_minus[i] != INT_MAX && dp_minus[i] <= next_val) {
            result[i+1] = dp_minus[i];
        } else {
             // This case should ideally not be reached if a solution exists.
             // We have to pick one, let's see which one is not MAX
             if(dp_plus[i] != INT_MAX) result[i+1] = dp_plus[i];
             else result[i+1] = dp_minus[i];
        }
    }
    
    free(dp_plus);
    free(dp_minus);
    return result;
}