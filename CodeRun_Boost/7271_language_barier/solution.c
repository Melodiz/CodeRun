#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    int unmatched_index;
    bool has_match_in_subtree;
} TrieNode;

int find_consume_and_update(TrieNode* node);

typedef struct {
    const char* word_ptr;
    int index;
} WordInfo;


int compare_word_info(const void* a, const void* b) {
    const WordInfo* info_a = (const WordInfo*)a;
    const WordInfo* info_b = (const WordInfo*)b;
    size_t len_a = strlen(info_a->word_ptr);
    size_t len_b = strlen(info_b->word_ptr);
    if (len_a < len_b) return 1;
    if (len_a > len_b) return -1;
    return 0;
}


TrieNode* create_new_node(TrieNode** arena, size_t* nodes_used) {
    TrieNode* new_node = &(*arena)[(*nodes_used)++];
    // Initialize all children to NULL.
    for (int i = 0; i < 26; i++) {
        new_node->children[i] = NULL;
    }
    new_node->unmatched_index = -1;
    new_node->has_match_in_subtree = false;
    return new_node;
}


int find_consume_and_update(TrieNode* node) {
    if (!node || !node->has_match_in_subtree) {
        return -1;
    }

    if (node->unmatched_index != -1) {
        int match_idx = node->unmatched_index;
        node->unmatched_index = -1; // Consume the match.


        node->has_match_in_subtree = false;
        for (int i = 0; i < 26; ++i) {
            if (node->children[i] && node->children[i]->has_match_in_subtree) {
                node->has_match_in_subtree = true;
                break; // Found one, no need to check further.
            }
        }
        return match_idx;
    }

    for (int i = 0; i < 26; ++i) {
        if (node->children[i]) {
            int match_idx = find_consume_and_update(node->children[i]);
            if (match_idx != -1) {
                // A match was found and consumed in a child's subtree.
                // We must now recalculate our own flag.
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

int** solve(int n, char **words) {
    int** result = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        result[i] = (int*)malloc(2 * sizeof(int));
    }

    size_t total_len = 0;
    for (int i = 0; i < 2 * n; i++) {
        total_len += strlen(words[i]);
    }
    TrieNode* node_arena = (TrieNode*)malloc((total_len + 2) * sizeof(TrieNode));
    size_t nodes_used = 0;


    WordInfo* words_info = (WordInfo*)malloc(2 * n * sizeof(WordInfo));
    for (int i = 0; i < 2 * n; ++i) {
        words_info[i].word_ptr = words[i];
        words_info[i].index = i;
    }

    qsort(words_info, 2 * n, sizeof(WordInfo), compare_word_info);

    TrieNode* root = create_new_node(&node_arena, &nodes_used);
    int pair_count = 0;

    for (int i = 0; i < 2 * n; i++) {
        const char* word = words_info[i].word_ptr;
        int index = words_info[i].index;

        TrieNode* current_node = root;
        for (const char* c = word; *c != '\0'; ++c) {
            current_node = current_node->children[*c - 'a'];
            if (!current_node) {
                break; // Path does not exist.
            }
        }
        
        int full_word_index = find_consume_and_update(current_node);
        
        if (full_word_index != -1) {
            // A match was found! Record the pair.
            result[pair_count][1] = full_word_index + 1;
            pair_count++;
        } else {
            current_node = root;
            for (const char* c = word; *c != '\0'; ++c) {
                int char_idx = *c - 'a';
                if (!current_node->children[char_idx]) {
                    current_node->children[char_idx] = create_new_node(&node_arena, &nodes_used);
                }
                current_node = current_node->children[char_idx];
                current_node->has_match_in_subtree = true;
            }
            current_node->unmatched_index = index;
        }
    }

    free(words_info);
    free(node_arena);

    return result;
}