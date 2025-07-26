#include <vector>
#include <algorithm> 

int solve(int n, const std::vector<int>& a, int m, const std::vector<int>& b) {
    std::vector<int> zeros_indices_a;
    std::vector<int> ones_indices_a;
    for (int i = 0; i < n; ++i) {
        if (a[i] == 0) {
            zeros_indices_a.push_back(i);
        } else {
            ones_indices_a.push_back(i);
        }
    }

    std::vector<int> zeros_indices_b;
    std::vector<int> ones_indices_b;
    for (int i = 0; i < m; ++i) {
        if (b[i] == 0) {
            zeros_indices_b.push_back(i);
        } else {
            ones_indices_b.push_back(i);
        }
    }

    int max_len = 0;
    int k_zeros = 0;
    int available_ones_a = ones_indices_a.size();
    int available_ones_b = ones_indices_b.size();
    int k_ones = std::min(available_ones_a, available_ones_b);
    max_len = std::max(max_len, k_zeros + k_ones);
    int max_possible_zeros = std::min((int)zeros_indices_a.size(), (int)zeros_indices_b.size());

    for (k_zeros = 1; k_zeros <= max_possible_zeros; ++k_zeros) {
        int last_zero_idx_a = zeros_indices_a[k_zeros - 1];
        
        int last_zero_idx_b = zeros_indices_b[k_zeros - 1];

        auto it_a = std::upper_bound(ones_indices_a.begin(), ones_indices_a.end(), last_zero_idx_a);
        available_ones_a = std::distance(it_a, ones_indices_a.end());

        auto it_b = std::upper_bound(ones_indices_b.begin(), ones_indices_b.end(), last_zero_idx_b);
        available_ones_b = std::distance(it_b, ones_indices_b.end());

        k_ones = std::min(available_ones_a, available_ones_b);
        
        int current_len = k_zeros + k_ones;
        max_len = std::max(max_len, current_len);
    }

    return max_len;
}