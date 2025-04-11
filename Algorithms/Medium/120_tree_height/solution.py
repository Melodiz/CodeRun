# Solution for https://coderun.yandex.ru/problem/tree-height/

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def add_node(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = add_node(root.left, value)
    elif value == root.value:
        return root
    else:
        root.right = add_node(root.right, value)
    return root

def solution():
    root = None
    values = list(map(int, input().split()))[:-1]
    for value in values:
        root = add_node(root, value)
    print(height(root))

if __name__ == "__main__":
    solution()
