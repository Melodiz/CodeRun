// Solution for https://coderun.yandex.ru/problem/1984-2/

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>

using namespace std;

struct AhoCorasickNode {
    unordered_map<char, AhoCorasickNode*> children;
    AhoCorasickNode* fail;
    bool is_end; // Marks the end of a stop word

    AhoCorasickNode() : fail(nullptr), is_end(false) {}
};

class AhoCorasick {
private:
    AhoCorasickNode* root;

    void build_trie(const vector<string>& patterns) {
        for (const string& word : patterns) {
            AhoCorasickNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new AhoCorasickNode();
                }
                node = node->children[c];
            }
            node->is_end = true; // Mark end of a stop word
        }
    }

    void build_fail_links() {
        queue<AhoCorasickNode*> q;
        root->fail = root;

        // Initialize fail links for root's children
        for (auto& pair : root->children) {
            pair.second->fail = root;
            q.push(pair.second);
        }

        // BFS to set fail links
        while (!q.empty()) {
            AhoCorasickNode* current = q.front();
            q.pop();

            for (auto& pair : current->children) {
                char c = pair.first;
                AhoCorasickNode* child = pair.second;
                AhoCorasickNode* fail = current->fail;

                while (fail != root && fail->children.find(c) == fail->children.end()) {
                    fail = fail->fail;
                }

                if (fail->children.find(c) != fail->children.end()) {
                    child->fail = fail->children[c];
                } else {
                    child->fail = root;
                }

                q.push(child);
            }
        }
    }

public:
    AhoCorasick(const vector<string>& patterns) {
        root = new AhoCorasickNode();
        build_trie(patterns);
        build_fail_links();
    }

    bool contains_stop_word(const string& text) {
        AhoCorasickNode* node = root;
        for (char c : text) {
            while (node != root && node->children.find(c) == node->children.end()) {
                node = node->fail;
            }

            if (node->children.find(c) != node->children.end()) {
                node = node->children[c];
            }

            if (node->is_end) {
                return true; // Early exit if any stop word is found
            }
        }
        return false;
    }

    ~AhoCorasick() {
        // Cleanup (optional for competitive programming)
        queue<AhoCorasickNode*> q;
        q.push(root);
        while (!q.empty()) {
            AhoCorasickNode* current = q.front();
            q.pop();
            for (auto& pair : current->children) {
                q.push(pair.second);
            }
            delete current;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    cin.ignore(); // Ignore newline after reading n and m

    vector<string> stop_words(n);
    for (int i = 0; i < n; ++i) {
        getline(cin, stop_words[i]);
    }

    AhoCorasick ac(stop_words);

    for (int i = 0; i < m; ++i) {
        string message;
        getline(cin, message);
        if (ac.contains_stop_word(message)) {
            cout << "DELETE\n";
        } else {
            cout << "KEEP\n";
        }
    }

    return 0;
}