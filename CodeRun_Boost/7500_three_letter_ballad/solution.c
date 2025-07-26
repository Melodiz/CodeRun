#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stddef.h>
#include <stdint.h>

long long solve(const char* ballad, int n) {
    int m = 0;
    for (int i = 0; i < n; ++i) {
        if (isalpha(ballad[i])) {
            m++;
        }
    }

    if (m < 3) {
        return 0;
    }

    char* letters = (char*)malloc(m * sizeof(char));
    if (letters == NULL) {
        return -1;
    }

    int letter_idx = 0;
    for (int i = 0; i < n; ++i) {
        if (isalpha(ballad[i])) {
            letters[letter_idx++] = ballad[i];
        }
    }

    long long* left_counts = (long long*)calloc(26, sizeof(long long));
    long long* right_counts = (long long*)calloc(26, sizeof(long long));

    if (left_counts == NULL || right_counts == NULL) {
        free(letters);
        free(left_counts);
        free(right_counts);
        return -1;
    }

    left_counts[letters[0] - 'a']++;
    for (int i = 2; i < m; ++i) {
        right_counts[letters[i] - 'a']++;
    }

    long long total_palindromes = 0;
    for (int j = 1; j < m - 1; ++j) {
        long long current_contribution = 0;
        for (int i = 0; i < 26; ++i) {
            current_contribution += left_counts[i] * right_counts[i];
        }
        total_palindromes += current_contribution;

        left_counts[letters[j] - 'a']++;
        right_counts[letters[j + 1] - 'a']--;
    }

    free(letters);
    free(left_counts);
    free(right_counts);

    return total_palindromes;
}