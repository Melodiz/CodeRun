from collections import defaultdict, deque


def build_adjacency_list(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def is_bipartite(graph, n):
    color = {}
    for vertex in range(1, n + 1):
        if vertex not in color:
            queue = deque([vertex])
            color[vertex] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True


def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = input().split()
        edges.append((int(a), int(b)))

    graph = build_adjacency_list(edges)

    if is_bipartite(graph, n):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
