#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void solution();
int* calculate_answer(int n, int* a);
int calculate_mex(const int* a, int start, int end);
bool check(int V, int n, const int* a);
int find_max(int n, const int* a);

void solution() {
    int t;
    if (scanf("%d", &t) != 1) return;

    for (int test = 0; test < t; ++test) {
        int n;
        if (scanf("%d", &n) != 1) return;

        int* a = (int*)malloc(n * sizeof(int));
        if (!a) return; 
        
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
        }

        int* answer = calculate_answer(n, a);

        if (answer) {
            for (int j = 0; j < 4; ++j) {
                printf("%d ", answer[j]);
            }
            printf("\n");
            free(answer);
        }
        
        free(a);
    }
}

int* calculate_answer(int n, int* a) {
    int* answer = (int*)malloc(4 * sizeof(int));
    if (!answer) return NULL;

    if (n == 1) {
        int m = (a[0] == 0) ? 1 : 0;
        answer[0] = m;
        answer[1] = m;
        answer[2] = m;
        answer[3] = m;
        return answer;
    }

    // --- General logic for n > 1 ---
    
    int mex_a = calculate_mex(a, 0, n - 1);
    int max_a = find_max(n, a);

    // 1. minMax (Binary Search for the answer)
    int low = 0, high = n;
    int min_max = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid, n, a)) {
            min_max = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
            
    // 2. maxMax
    int max_max = (max_a > mex_a) ? max_a : mex_a;
    
    // 3. minMin
    int min_min = 0;
    
    // 4. maxMin
    int max_min = mex_a;
    
    // Assemble the final answer
    answer[0] = min_max;    
    answer[1] = max_max;
    answer[2] = min_min;
    answer[3] = max_min;

    return answer;
}

int calculate_mex(const int* a, int start, int end) {
    if (start > end) return 0;
    
    int length = end - start + 1;
    bool* seen = (bool*)calloc(length + 1, sizeof(bool));
    if (!seen) return -1;

    for (int i = start; i <= end; ++i) {
        int val = a[i];
        if (val >= 0 && val <= length) {
            seen[val] = true;
        }
    }

    int mex = 0;
    while (mex <= length && seen[mex]) {
        mex++;
    }

    free(seen);
    return mex;
}

bool check(int V, int n, const int* a) {
    int l0 = -1, r0 = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] > V) {
            if (l0 == -1) l0 = i;
            r0 = i;
        }
    }

    if (l0 == -1) {
        bool has_non_zero = false;
        for (int i = 0; i < n; ++i) {
            if (a[i] != 0) {
                has_non_zero = true;
                break;
            }
        }
        if (has_non_zero) return true;
        return V >= 1;
    } else {
        int m = calculate_mex(a, l0, r0);
        return m <= V;
    }
}

int find_max(int n, const int* a) {
    if (n <= 0) return 0;
    
    int max_val = a[0];
    for (int i = 1; i < n; ++i) {
        if (a[i] > max_val) {
            max_val = a[i];
        }
    }
    return max_val;
}