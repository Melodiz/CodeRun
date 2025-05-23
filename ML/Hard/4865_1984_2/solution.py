# Solution for https://coderun.yandex.ru/problem/1984-2/
from collections import deque

class AhoCorasickNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.is_end = False  # Marks end of a stop word

def build_trie(stop_words):
    root = AhoCorasickNode()
    for word in stop_words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = AhoCorasickNode()
            node = node.children[char]
        node.is_end = True  # Mark end of stop word
    return root

def build_fail_links(root):
    queue = deque()
    root.fail = root
    for child in root.children.values():
        child.fail = root
        queue.append(child)
    while queue:
        current = queue.popleft()
        for char, child in current.children.items():
            fail = current.fail
            while fail != root and char not in fail.children:
                fail = fail.fail
            if char in fail.children:
                child.fail = fail.children[char]
            else:
                child.fail = root
            queue.append(child)
    return root

def contains_stop_word(message, root):
    node = root
    for char in message:
        while node != root and char not in node.children:
            node = node.fail
        if char in node.children:
            node = node.children[char]
        if node.is_end:
            return True  # Early exit on first match
    return False


def solution():
    # Input
    n, m = map(int, input().split())
    stop_words = [input().strip() for _ in range(n)]
    messages = [input().strip() for _ in range(m)]

    # Preprocess
    root = build_trie(stop_words)
    root = build_fail_links(root)

    # Process messages
    for message in messages:
        if contains_stop_word(message, root):
            print("KEEP")  
        else:
            print("DELETE")

if __name__ == "__main__":
    solution()
