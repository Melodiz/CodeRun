#include <iostream>
#include <vector>
#include <algorithm>

struct Node
{
    int value;
    Node *left;
    Node *right;

    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

Node *insert(Node *root, int value)
{
    if (root == nullptr)
    {
        return new Node(value);
    }
    if (value == root->value)
    {
        return root;
    }
    if (value <= root->value)
    {
        root->left = insert(root->left, value);
    }
    else
    {
        root->right = insert(root->right, value);
    }

    return root;
}

int height(Node *node)
{
    if (node == nullptr)
    {
        return 0;
    }

    return std::max(height(node->left), height(node->right)) + 1;
}

bool is_balanced(Node *node)
{
    if (node == nullptr)
    {
        return true;
    }

    int left_height = height(node->left);
    int right_height = height(node->right);

    if (std::abs(left_height - right_height) <= 1 &&
        is_balanced(node->left) &&
        is_balanced(node->right))
    {
        return true;
    }

    return false;
}

int main()
{
    // Read input sequence
    std::vector<int> numbers;
    int num;

    while (std::cin >> num && num != 0)
    {
        numbers.push_back(num);
    }

    Node *root = nullptr;
    for (int num : numbers)
    {
        root = insert(root, num);
    }

    if (is_balanced(root))
    {
        std::cout << "YES" << std::endl;
    }
    else
    {
        std::cout << "NO" << std::endl;
    }

    return 0;
}