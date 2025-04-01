class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value == root.value:
        return root
    if value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

def height(node):
    if node is None:
        return 0
    
    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    if node is None:
        return True
    
    left_height = height(node.left)
    right_height = height(node.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    
    return False

def main():
    # Read input sequence
    numbers = list(map(int, input().split()))[:-1]
    
    # Build the tree
    root = None
    for num in numbers:
        root = insert(root, num)
    
    # Check if the tree is balanced
    if is_balanced(root):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()