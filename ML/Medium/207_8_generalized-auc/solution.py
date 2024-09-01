class Node:
    def __init__(self, x):
        self.x = x
        self.left_count = 0
        self.right_count = 0
        self.n = 1
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            cur = self.root
            while True:
                if x == cur.x:
                    cur.n += 1
                    break
                elif x < cur.x:
                    cur.left_count += 1
                    if cur.left is None:
                        cur.left = Node(x)
                        break
                    else:
                        cur = cur.left
                else:
                    cur.right_count += 1
                    if cur.right is None:
                        cur.right = Node(x)
                        break
                    else:
                        cur = cur.right

    def count_less_and_eq(self, x):
        less = 0
        eq = 0
        cur = self.root
        while cur:
            if x == cur.x:
                less += cur.left_count
                eq = cur.n
                break
            elif x < cur.x:
                cur = cur.left
            else:
                less += cur.left_count + cur.n
                cur = cur.right
        return less, eq
    
    
with open('input.txt', 'r') as file:
    n = int(file.readline())
    arr = []
    for _ in range(n):
        true_val, prev_val = map(float, file.readline().split())
        arr.append((true_val, prev_val))

arr.sort(key=lambda x: x[0])

tree = BinaryTree()
num = 0
denom = 0

i = 0
while i < n:
    j = i
    while j < n and arr[i][0] == arr[j][0]:
        r = tree.count_less_and_eq(arr[j][1])
        num += r[0] + r[1] / 2
        denom += i
        j += 1

    for k in range(i, j):
        tree.add(arr[k][1])

    i = j

print(num / denom)