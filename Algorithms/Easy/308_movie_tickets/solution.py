# Solution for https://coderun.yandex.ru/problem/movie-tickets
# Other solutions: https://github.com/Melodiz/CodeRun

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

def main():
    uf = UnionFind()
    data = []
    with open("Algorithms/Easy/308_movie_tickets/logs.csv", "r") as file:
        for line in file:
            email, phone = line.strip().split(",")
            data.append((email, phone))
            uf.union(email, phone)
    
    # Now, count the occurrences of each root
    root_counts = {}
    for email, phone in data:
        root = uf.find(email)
        root_counts[root] = root_counts.get(root, 0) + 1
    
    if not root_counts:
        print(0)
    else:
        print(max(root_counts.values()))

if __name__ == "__main__":
    # Maybe it's overcomplicated for <3000rows, but it's second idea I've had.
    main()