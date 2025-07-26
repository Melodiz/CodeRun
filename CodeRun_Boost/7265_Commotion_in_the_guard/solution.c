#include <stdlib.h>
#include <stdbool.h>

int* solution(int n, int m, int* swap_values) {
    int* positions = (int*)malloc((2 * n) * sizeof(int));
    if (positions == NULL) {
        return NULL;
    }
    for (int i = 0; i < (2 * n); i++) {
        positions[i] = i + 1;
    }

    int methods_on_left_count = n;

    int* results = (int*)malloc(m * sizeof(int));
    if (results == NULL) {
        free(positions);
        return NULL;
    }

    for (int i = 0; i < m; i++) {
        int p1_orig = swap_values[2 * i];
        int p2_orig = swap_values[2 * i + 1];

        int p1_idx = p1_orig - 1;
        int p2_idx = p2_orig - 1;

        bool p1_is_left = (p1_idx < n);
        bool p2_is_left = (p2_idx < n);

        if (p1_is_left != p2_is_left) {
            int guard1 = positions[p1_idx];
            int guard2 = positions[p2_idx];
            
            bool guard1_is_method = (guard1 <= n);
            bool guard2_is_method = (guard2 <= n);

            if (p1_is_left) {
                if (guard1_is_method) {
                    methods_on_left_count--;
                }
                if (guard2_is_method) {
                    methods_on_left_count++;
                }
            } else {
                if (guard2_is_method) {
                    methods_on_left_count--;
                }
                if (guard1_is_method) {
                    methods_on_left_count++;
                }
            }
        }

        int temp = positions[p1_idx];
        positions[p1_idx] = positions[p2_idx];
        positions[p2_idx] = temp;

        results[i] = methods_on_left_count;
    }

    free(positions);

    return results;
}