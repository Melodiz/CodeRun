#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_N 100

int n;
int graph[MAX_N][MAX_N];
bool visited[MAX_N];
int path[MAX_N];
int path_size = 0;

int* dfs(int node, int parent) {
    visited[node] = true;
    path[path_size++] = node;

    for (int neighbor = 0; neighbor < n; neighbor++) {
        if (graph[node][neighbor] == 1) {  // If there's an edge
            if (!visited[neighbor]) {
                int* cycle = dfs(neighbor, node);
                if (cycle != NULL) {
                    return cycle;
                }
            } else if (neighbor != parent) {
                // Cycle detected
                int cycle_start;
                for (cycle_start = 0; cycle_start < path_size; cycle_start++) {
                    if (path[cycle_start] == neighbor) break;
                }
                
                int* cycle = (int*)malloc((path_size - cycle_start + 1) * sizeof(int));
                int cycle_index = 0;
                for (int i = cycle_start; i < path_size; i++) {
                    cycle[cycle_index++] = path[i];
                }
                cycle[cycle_index] = neighbor;
                return cycle;
            }
        }
    }

    path_size--;
    return NULL;
}

int* find_cycle() {
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    path_size = 0;

    for (int node = 0; node < n; node++) {
        if (!visited[node]) {
            int* cycle = dfs(node, -1);
            if (cycle != NULL) {
                return cycle;
            }
        }
    }

    return NULL;
}

int main() {
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    int* cycle = find_cycle();

    if (cycle != NULL) {
        int cycle_length = 1;
        while (cycle[cycle_length] != cycle[0]) {
            cycle_length++;
        }

        printf("YES\n");
        printf("%d\n", cycle_length);
        for (int i = 0; i < cycle_length; i++) {
            printf("%d", cycle[i] + 1);
            if (i < cycle_length - 1) {
                printf(" ");
            }
        }
        printf("\n");

        free(cycle);
    } else {
        printf("NO\n");
    }

    return 0;
}