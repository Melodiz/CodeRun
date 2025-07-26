#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

void solve_test_case() {
    int n;
    scanf("%d", &n);

    int *adj = (int*)malloc((n + 1) * sizeof(int));    // adj[i] stores the node that i points to.
    int *costs = (int*)malloc((n + 1) * sizeof(int));  // costs[i] stores the cost b[i].
    

    int *visited = (int*)calloc(n + 1, sizeof(int)); // calloc initializes memory to zero.

    for (int i = 0; i < n; i++) {
        int target_node;
        scanf("%d", &target_node);
        adj[i + 1] = target_node; // Node (i+1) points to target_node.
    }

    for (int i = 0; i < n; i++) {
        int cost_value;
        scanf("%d", &cost_value);
        costs[i + 1] = cost_value; // Cost for changing the edge from (i+1).
    }

    long long *all_cycle_min_b_values = (long long*)malloc(n * sizeof(long long));
    int k = 0; // Counter for the number of cycles found.

    for (int i = 1; i <= n; i++) {
        if (visited[i] == 0) {
            int current_node = i;
            
            int *path_nodes = (int*)malloc(n * sizeof(int));
            int path_len = 0;

            while (visited[current_node] == 0) {
                visited[current_node] = 1; // Mark as 'visiting'.
                path_nodes[path_len++] = current_node;
                current_node = adj[current_node];
            }

            if (visited[current_node] == 1) {
                int cycle_start_index = -1;
                for (int j = 0; j < path_len; j++) {
                    if (path_nodes[j] == current_node) {
                        cycle_start_index = j;
                        break;
                    }
                }

                if (cycle_start_index != -1) {
                    int min_b_for_this_cycle = INT_MAX;
                    for (int j = cycle_start_index; j < path_len; j++) {
                        int node_in_cycle = path_nodes[j];
                        if (costs[node_in_cycle] < min_b_for_this_cycle) {
                            min_b_for_this_cycle = costs[node_in_cycle];
                        }
                    }
                    all_cycle_min_b_values[k++] = min_b_for_this_cycle;
                }
            }

            for (int j = 0; j < path_len; j++) {
                visited[path_nodes[j]] = 2;
            }
            free(path_nodes); // Free the memory for the path tracker.
        }
    }

    long long total_cost = 0;

    if (k > 1) {
         for (int i = 0; i < k; i++) {
            total_cost += all_cycle_min_b_values[i];
        }
    }
    
    printf("%lld\n", total_cost);

    free(adj);
    free(costs);
    free(visited);
    free(all_cycle_min_b_values);
}

// не изменяйте сигнатуру метода
void solution() {
   int num_test_cases;
   scanf("%d", &num_test_cases);
   while (num_test_cases--) {
       solve_test_case();
   }
}