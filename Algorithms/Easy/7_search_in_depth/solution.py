from collections import defaultdict


def build_adjacency_list(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs(graph, start, visited):
    stack = [start]
    component = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            stack.extend(set(graph[vertex]) - visited)

    return component


def find_component_with_vertex_1(edges):
    graph = build_adjacency_list(edges)
    visited = set()
    component = dfs(graph, 1, visited)
    return component

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = find_component_with_vertex_1(edges)
    print(len(result))
    print(*sorted(result))


if __name__ == "__main__":
    main()
