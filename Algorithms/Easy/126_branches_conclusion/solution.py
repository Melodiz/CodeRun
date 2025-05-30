# Solution for https://coderun.yandex.ru/problem/branches-conclusion
# Other solutions: https://github.com/Melodiz/CodeRun

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
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def find_leaves(root, leaves):
    if root is None:
        return
    if (root.left and root.right is None) or (root.left is None and root.right):
        leaves.append(root.value)
    find_leaves(root.left, leaves)
    find_leaves(root.right, leaves)

def main():
    arr = list(map(int, input().split()))[:-1]
    root = None
    for num in arr:
        root = insert(root, num)
    leaves = []
    find_leaves(root, leaves)
    for val in sorted(leaves):
        print(val)

if __name__ == "__main__":
    main()
