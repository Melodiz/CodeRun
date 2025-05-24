// Solution for https://coderun.yandex.ru/problem/depth-added-elements/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <set>

// implementation of BinarySearchTree
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
    bool isLeaf() const {
        return left == nullptr && right == nullptr;
    }
};

Node* Insert(Node* root, int value) {
    if (root == nullptr) {
        return new Node(value);
    }

    if (value < root->value) {
        root->left = Insert(root->left, value);
    } else if (value > root->value) {
        root->right = Insert(root->right, value);
    }
    return root;
}

// Function to find the depth of a specific node
int FindNodeDepth(Node* root, int value, int currentDepth = 1) {
    if (root == nullptr) {
        return 0; // Node not found
    }
    
    if (root->value == value) {
        return currentDepth;
    }
    
    if (value < root->value) {
        return FindNodeDepth(root->left, value, currentDepth + 1);
    } else {
        return FindNodeDepth(root->right, value, currentDepth + 1);
    }
}

int main()
{
    vector<int> values;
    set<int> seen;
    while (true) {
        int value;
        cin >> value;
        if (value == 0)
        {
            break;
        }
        if (seen.find(value)!=seen.end()) {
            continue;
        }
        values.push_back(value);
        seen.insert(value);
    }
    
    Node* root = nullptr;
    for (int value : values) {
        root = Insert(root, value);
    }
    
    for (int value : values) {
        int depth = FindNodeDepth(root, value);
        cout << depth << " ";
    }
    
    return 0;
}