#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int solution(int n, int* a) {
    qsort(a, n, sizeof(int), compare);

    int left = 0;
    int max_keep = 0;

    for (int right = 0; right < n; right++) {
        while (a[right] - a[left] >= n) {
            left++;
        }

        int current_keep = right - left + 1;
        
        if (current_keep > max_keep) {
            max_keep = current_keep;
        }
    }

    int min_moves = n - max_keep;
    return min_moves;
}