#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int m;
    int** matrix;
} matrixData;

typedef struct {
    int value;
    char* path;
} Result;

matrixData read_input() {
    matrixData data;
    scanf("%d %d", &data.n, &data.m);

    // Allocate memory for the matrix
    data.matrix = (int**)malloc(data.n * sizeof(int*));
    for (int i = 0; i < data.n; i++) {
        data.matrix[i] = (int*)malloc(data.m * sizeof(int));
    }

    // Read the matrix values
    for (int i = 0; i < data.n; i++) {
        for (int j = 0; j < data.m; j++) {
            scanf("%d", &data.matrix[i][j]);
        }
    }

    return data;
}

Result solve(matrixData data, int n, int m) {
    // create a n by m matrix with all zeros
    int **dp;
    dp = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dp[i] = (int*)calloc(m, sizeof(int));
    }
    // create a matrix (history) of n by m chars with initial value 'R'
    char **history;
    history = (char**)malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        history[i] = (char*)malloc(m * sizeof(char));
        for (int j = 0; j < m; j++) {
            history[i][j] = 'R';
        }
    }
    // initialize the first row 
    dp[0][0] = data.matrix[0][0];
    for (int j = 1; j < m; j++) {
        dp[0][j] = dp[0][j - 1] + data.matrix[0][j];
        history[0][j] = 'R';
    }
    // initialize the first column
    for (int i = 1; i < n; i++) {
        dp[i][0] = dp[i-1][0] + data.matrix[i][0];
        history[i][0] = 'D';
    }

    // Fill the rest of dp and history
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (dp[i-1][j] > dp[i][j-1]) {
                dp[i][j] = dp[i-1][j] + data.matrix[i][j];
                history[i][j] = 'D';
            } else {
                dp[i][j] = dp[i][j-1] + data.matrix[i][j];
                history[i][j] = 'R';
            }
        }
    }

    // backtrack to find the path
    char *path = (char*)malloc((n + m - 1) * sizeof(char));
    int i = n - 1, j = m - 1;
    int k = n + m - 2;
    path[k] = '\0';
    while (i > 0 || j > 0) {
        k--;
        if (i > 0 && (j == 0 || dp[i-1][j] > dp[i][j-1])) {
            path[k] = 'D';
            i--;
        } else {
            path[k] = 'R';
            j--;
        }
    }
    Result result = {dp[n-1][m-1], path};

    // Free allocated memory
    for (int i = 0; i < n; i++) {
        free(dp[i]);
        free(history[i]);
    }
    free(dp);
    free(history);

    return result;
}

int main()
{
    matrixData data = read_input();
    Result result = solve(data, data.n, data.m);
    printf("%d\n", result.value);
    
    // Print path with each character separated by space
    for (int i = 0; result.path[i] != '\0'; i++) {
        printf("%c", result.path[i]);
        if (result.path[i+1] != '\0') {
            printf(" ");
        }
    }
    printf("\n");

    // Free allocated memory
    for (int i = 0; i < data.n; i++) {
        free(data.matrix[i]);
    }
    free(data.matrix);
    free(result.path);

    return 0;
}