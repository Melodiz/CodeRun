#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <iostream>

struct TrieNode {
    TrieNode* children[26] = {};
    int unmatched_index = -1;
    bool has_match_in_subtree = false;
};

int find_consume_and_update(TrieNode* node) {
    if (!node || !node->has_match_in_subtree) {
        return -1;
    }

    if (node->unmatched_index != -1) {
        int match_idx = node->unmatched_index;
        node->unmatched_index = -1; // Consume the match.
        node->has_match_in_subtree = false; // It might have children with matches, so check them.
        for (int i = 0; i < 26; ++i) {
            if (node->children[i] && node->children[i]->has_match_in_subtree) {
                node->has_match_in_subtree = true;
                break;
            }
        }
        return match_idx;
    }

    // Recursive Step: Search in promising subtrees.
    for (int i = 0; i < 26; ++i) {
        if (node->children[i]) {
            int match_idx = find_consume_and_update(node->children[i]);
            if (match_idx != -1) {
                // A match was consumed below. Recalculate our own flag now.
                node->has_match_in_subtree = false;
                for (int j = 0; j < 26; ++j) {
                    if (node->children[j] && node->children[j]->has_match_in_subtree) {
                        node->has_match_in_subtree = true;
                        break;
                    }
                }
                return match_idx;
            }
        }
    }

    return -1;
}

std::vector<std::pair<int, int>> solve(int n, const std::vector<std::string>& words) {
    // This setup is for speed in competitive programming environments.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::vector<std::pair<int, int>> result(n);

    size_t total_len = 0;
    for (const auto& s : words) total_len += s.length();
    std::vector<TrieNode> node_arena(total_len + 2);
    size_t nodes_used = 0;
    auto get_new_node = [&]() { return &node_arena[nodes_used++]; };

    struct WordInfo { const std::string* word_ptr; int index; };
    std::vector<WordInfo> words_info(2 * n);
    for (int i = 0; i < 2 * n; ++i) words_info[i] = {&words[i], i};
    std::sort(words_info.begin(), words_info.end(), 
        [](const auto& a, const auto& b) { return a.word_ptr->length() > b.word_ptr->length(); });

    TrieNode* root = get_new_node();
    int pair_count = 0;

    for (const auto& info : words_info) {
        const std::string& word = *info.word_ptr;
        int index = info.index;

        TrieNode* current_node = root;
        for (char c : word) {
            current_node = current_node->children[c - 'a'];
            if (!current_node) break;
        }
        
        int full_word_index = find_consume_and_update(current_node);
        
        if (full_word_index != -1) {
            result[pair_count++] = {index + 1, full_word_index + 1};
        } else {
            // No match found, so insert this as a full word.
            current_node = root;
            TrieNode* path_node = root;
            for (char c : word) {
                int char_idx = c - 'a';
                if (!path_node->children[char_idx]) {
                    path_node->children[char_idx] = get_new_node();
                }
                path_node = path_node->children[char_idx];
                path_node->has_match_in_subtree = true; // Set flag on the path.
            }
            path_node->unmatched_index = index;
        }
    }

    return result;
}