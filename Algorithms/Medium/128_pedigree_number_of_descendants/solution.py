# Solution for https://coderun.yandex.ru/problem/pedigree-number-of-descendants
# Other solutions: https://github.com/Melodiz/CodeRun
from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(100000)

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    @lru_cache(maxsize=None)
    def get_number_of_descendants(self):
        return sum(child.get_number_of_descendants() for child in self.children) + 1

def main():
    n = int(input())
    nodes = {}
    for _ in range(n-1):
        child, parent = input().split()
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child, nodes[parent])
        nodes[parent].add_child(nodes[child])
    
    for node in sorted(nodes.values(), key=lambda x: x.name):
        print(node.name, node.get_number_of_descendants() - 1)
    

if __name__ == "__main__":
    main()
