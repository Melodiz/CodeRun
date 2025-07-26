#include <stdio.h>   
#include <stdlib.h>  
#include <string.h>  

int count_le(const int* arr, int size, int value) {
    int low = 0;
    int high = size;
    int ans_idx = 0; 

    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= value) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low; 
}


int solve(int n, const int* a, int m, const int* b) {

    int* zeros_indices_a = (int*)malloc(n * sizeof(int));
    int* ones_indices_a = (int*)malloc(n * sizeof(int));
    int zeros_count_a = 0;
    int ones_count_a = 0;

    for (int i = 0; i < n; ++i) {
        if (a[i] == 0) {
            zeros_indices_a[zeros_count_a++] = i;
        } else {
            ones_indices_a[ones_count_a++] = i;
        }
    }

    int* zeros_indices_b = (int*)malloc(m * sizeof(int));
    int* ones_indices_b = (int*)malloc(m * sizeof(int));
    int zeros_count_b = 0;
    int ones_count_b = 0;

    for (int i = 0; i < m; ++i) {
        if (b[i] == 0) {
            zeros_indices_b[zeros_count_b++] = i;
        } else {
            ones_indices_b[ones_count_b++] = i;
        }
    }

    int max_len = 0;

    int k_zeros = 0;
    int available_ones_a = ones_count_a;
    int available_ones_b = ones_count_b;
    int k_ones = (available_ones_a < available_ones_b) ? available_ones_a : available_ones_b; // std::min
    max_len = (max_len > (k_zeros + k_ones)) ? max_len : (k_zeros + k_ones); 

    int max_possible_zeros = (zeros_count_a < zeros_count_b) ? zeros_count_a : zeros_count_b; // std::min

    for (k_zeros = 1; k_zeros <= max_possible_zeros; ++k_zeros) {
        int last_zero_idx_a = zeros_indices_a[k_zeros - 1];
        int last_zero_idx_b = zeros_indices_b[k_zeros - 1];

        int idx_of_first_one_after_last_zero_a = count_le(ones_indices_a, ones_count_a, last_zero_idx_a);
        available_ones_a = ones_count_a - idx_of_first_one_after_last_zero_a;

        int idx_of_first_one_after_last_zero_b = count_le(ones_indices_b, ones_count_b, last_zero_idx_b);
        available_ones_b = ones_count_b - idx_of_first_one_after_last_zero_b;

        k_ones = (available_ones_a < available_ones_b) ? available_ones_a : available_ones_b; // std::min
        int current_len = k_zeros + k_ones;
        max_len = (max_len > current_len) ? max_len : current_len; 
    }

    free(zeros_indices_a);
    free(ones_indices_a);
    free(zeros_indices_b);
    free(ones_indices_b);

    return max_len;
}