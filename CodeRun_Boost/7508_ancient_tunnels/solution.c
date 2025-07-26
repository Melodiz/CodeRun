#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Forward declarations are good practice but not strictly necessary if functions are defined before use.
void calculate_answer(int n, int* a);
int get_tree_sz(int u, int* memo, int** rev_adj, const int* in_degree, const bool* is_in_cycle);
int get_dag_sz(int u, int* memo, int** rev_adj, const int* in_degree, const bool* is_in_component);


void solution() {
    int t;
    if (scanf("%d", &t) != 1) return;

    for (int test = 0; test < t; ++test) {
        int n;
        if (scanf("%d", &n) != 1) return;

        int* a = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
        }

        calculate_answer(n, a);

        free(a);
    }
}

void calculate_answer(int n, int* a) {
    // 1. MEMORY ALLOCATION & GRAPH REPRESENTATION
    int* adj = (int*)malloc(n * sizeof(int));
    int* state = (int*)calloc(n, sizeof(int)); // 0=unvisited, 1=visiting, 2=finished
    int* ans = (int*)malloc(n * sizeof(int));
    
    int** rev_adj = (int**)malloc(n * sizeof(int*));
    int* in_degree = (int*)calloc(n, sizeof(int));
    
    int* path = (int*)malloc(n * sizeof(int));
    bool* is_in_cycle = (bool*)calloc(n, sizeof(bool));
    int* q = (int*)malloc(n * sizeof(int));
    int* memo = (int*)malloc(n * sizeof(int));
    bool* is_in_component = (bool*)calloc(n, sizeof(bool));

    // 2. BUILD GRAPHS
    for (int i = 0; i < n; ++i) {
        adj[i] = a[i] - 1; 
        if (adj[i] >= 0) {
            in_degree[adj[i]]++;
        }
    }

    for (int i = 0; i < n; ++i) {
        rev_adj[i] = (int*)malloc(in_degree[i] * sizeof(int));
    }
    int* in_degree_counters = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (adj[i] >= 0) {
            int target = adj[i];
            rev_adj[target][in_degree_counters[target]++] = i;
        }
    }
    free(in_degree_counters);

    // 3. MAIN LOGIC: PROCESS COMPONENTS
    for (int i = 0; i < n; ++i) {
        if (state[i] == 2) continue;

        int path_size = 0;
        int curr = i;
        while (curr != -2 && state[curr] == 0) {
            state[curr] = 1; 
            path[path_size++] = curr;
            curr = adj[curr];
        }

        bool cycle_found = false;
        memset(is_in_cycle, false, n * sizeof(bool));
        if (curr != -2 && state[curr] == 1) {
            cycle_found = true;
            for (int j = 0; j < path_size; ++j) {
                if (path[j] == curr) {
                    for (int k = j; k < path_size; ++k) {
                        is_in_cycle[path[k]] = true;
                    }
                    break;
                }
            }
        }

        int q_head = 0, q_tail = 0;
        memset(is_in_component, false, n * sizeof(bool));
        for (int j = 0; j < path_size; ++j) {
            int node_on_path = path[j];
            if (!is_in_component[node_on_path]) {
                 q[q_tail++] = node_on_path;
                 is_in_component[node_on_path] = true;
            }
        }
        while (q_head < q_tail) {
            int u = q[q_head++];
            for (int j = 0; j < in_degree[u]; ++j) {
                int v_pred = rev_adj[u][j];
                if (!is_in_component[v_pred]) {
                    is_in_component[v_pred] = true;
                    q[q_tail++] = v_pred;
                }
            }
        }
        int component_size = q_tail;

        for(int j = 0; j < component_size; ++j) {
            state[q[j]] = 2;
        }

        memset(memo, -1, n * sizeof(int));
        if (cycle_found) {
            for (int j = 0; j < component_size; ++j) {
                int node = q[j];
                ans[node] = is_in_cycle[node] ? component_size : get_tree_sz(node, memo, rev_adj, in_degree, is_in_cycle);
            }
        } else {
            for (int j = 0; j < component_size; ++j) {
                get_dag_sz(q[j], memo, rev_adj, in_degree, is_in_component);
            }
            for (int j = 0; j < component_size; ++j) {
                ans[q[j]] = memo[q[j]];
            }
        }
    }
    
    for (int i = 0; i < n; ++i) {
        printf("%d%c", ans[i], (i == n - 1) ? '\n' : ' ');
    }

    free(adj);
    free(state);
    free(ans);
    for (int i = 0; i < n; ++i) {
        free(rev_adj[i]);
    }
    free(rev_adj);
    free(in_degree);
    free(path);
    free(is_in_cycle);
    free(q);
    free(memo);
    free(is_in_component);
}

int get_tree_sz(int u, int* memo, int** rev_adj, const int* in_degree, const bool* is_in_cycle) {
    if (memo[u] != -1) return memo[u];
    if (is_in_cycle[u]) return memo[u] = 0;

    int size = 1;
    for (int i = 0; i < in_degree[u]; ++i) {
        size += get_tree_sz(rev_adj[u][i], memo, rev_adj, in_degree, is_in_cycle);
    }
    return memo[u] = size;
}

int get_dag_sz(int u, int* memo, int** rev_adj, const int* in_degree, const bool* is_in_component) {
    if (memo[u] != -1) return memo[u];

    int size = 1;
    for (int i = 0; i < in_degree[u]; ++i) {
        int v_pred = rev_adj[u][i];
        if (is_in_component[v_pred]) {
             size += get_dag_sz(v_pred, memo, rev_adj, in_degree, is_in_component);
        }
    }
    return memo[u] = size;
}