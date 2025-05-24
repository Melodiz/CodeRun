# Solution for https://coderun.yandex.ru/problem/depth-added-elements/

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:  # Skip if value already exists
        root.right = insert(root.right, value)
    return root

def find_node_depth(root, value, depth=1):
    if root is None:
        return 0
    if root.value == value:
        return depth
    if value < root.value:
        return find_node_depth(root.left, value, depth + 1)
    else:
        return find_node_depth(root.right, value, depth + 1)

def solution():
    seen = set()
    root = None
    for value in map(int, input().split()):
        if value == 0:
            break
        if value not in seen:
            seen.add(value)
            root = insert(root, value)
            print(find_node_depth(root, value), end=' ')

if __name__ == "__main__":
    solution()