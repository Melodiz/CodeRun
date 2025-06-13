// Solution for https://coderun.yandex.ru/problem/pedigree-number-of-descendants
// Other solutions: https://github.com/Melodiz/CodeRun
#include <iostream>
#include <vector>
#include <unordered_map>

class Node {
    public:
        std::string name;
        std::vector<Node*> children;
        Node(std::string name) : name(name) {}
        void add_child(Node* child) {
            children.push_back(child);
        }
        int get_number_of_descendants() {
            int count = 1;
            for (Node* child : children) {
                count += child->get_number_of_descendants();
            }
            return count;
        }
};

int main() {
    int n;
    std::cin >> n;
    std::unordered_map<std::string, Node*> nodes;
    for (int i = 0; i < n - 1; i++) {
        std::string child, parent;
        std::cin >> child >> parent;
        if (nodes.find(parent) == nodes.end()) {
            nodes[parent] = new Node(parent);
        }
        if (nodes.find(child) == nodes.end()) {
            nodes[child] = new Node(child);
        }
        nodes[parent]->add_child(nodes[child]);
    }
    std::vector<Node*> nodes_vector;
    for (auto& node : nodes) {
        nodes_vector.push_back(node.second);
    }
    std::sort(nodes_vector.begin(), nodes_vector.end(), [](Node* a, Node* b) {
        return a->name < b->name;
    });
    for (auto& node : nodes_vector) {
        std::cout << node->name << " " << node->get_number_of_descendants() - 1 << std::endl;
    }
}