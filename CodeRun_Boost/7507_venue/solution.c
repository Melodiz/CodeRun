#include <stdio.h>
#include <stdlib.h>  
#include <time.h>    
#include <stdbool.h> 

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    size_t first;
    size_t second;
} Pair;


static long long dist_sq(Point p1, Point p2) {
    long long dx = (long long)p1.x - p2.x;
    long long dy = (long long)p1.y - p2.y;
    return dx * dx + dy * dy;
}


static void shuffle_indices(size_t* array, size_t n) {
    if (n > 1) {
        for (size_t i = n - 1; i > 0; i--) {
            size_t j = rand() % (i + 1);
            size_t temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}



Pair calculate_answer(int n, Point* points) {
    if (n == 2) {
        return (Pair){1, 2};
    }

    srand(time(NULL));

    size_t* indices = malloc(n * sizeof(size_t));
    if (!indices) {
        return (Pair){0, 0};
    }
    for (size_t i = 0; i < n; ++i) {
        indices[i] = i;
    }
    shuffle_indices(indices, n);

    int num_attempts = (n < 40) ? n : 40;

    for (int i = 0; i < num_attempts; ++i) {
        size_t anchor_idx = indices[i];
        
        long long min_dist_sq = -1;
        size_t neighbor_idx = 0;

        for (size_t j = 0; j < n; ++j) {
            if (j == anchor_idx) continue;
            
            long long d_sq = dist_sq(points[anchor_idx], points[j]);
            
            if (min_dist_sq == -1 || d_sq < min_dist_sq) {
                min_dist_sq = d_sq;
                neighbor_idx = j;
            }
        }

        bool is_valid_pair = true;
        for (size_t k = 0; k < n; ++k) {
            if (k == anchor_idx || k == neighbor_idx) continue;
            
            if (dist_sq(points[k], points[anchor_idx]) == dist_sq(points[k], points[neighbor_idx])) {
                is_valid_pair = false;
                break;
            }
        }
        
        if (is_valid_pair) {
            free(indices);
            return (Pair){anchor_idx + 1, neighbor_idx + 1};
        }
    }

    free(indices);
    return (Pair){0, 0};
}


// --- Provided I/O Boilerplate ---

void solution() {
    int n;
    scanf("%d", &n);

    Point* points = malloc(n * sizeof(Point));
    if (!points) return; 

    for (int i = 0; i < n; ++i) {
        scanf("%d %d", &points[i].x, &points[i].y);
    }

    Pair answer = calculate_answer(n, points);
    printf("%zu %zu\n", answer.first, answer.second);

    free(points);
}
