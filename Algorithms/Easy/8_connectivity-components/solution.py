from collections import defaultdict

def build_adjacency_list(edges, n):
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

def find_all_components(n, edges):
    graph = build_adjacency_list(edges, n)
    visited = set()
    components = []

    for vertex in range(1, n + 1):
        if vertex not in visited:
            component = dfs(graph, vertex, visited)
            components.append(component)

    return components

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    components = find_all_components(n, edges)
    
    print(len(components))
    for component in components:
        print(len(component))
        print(*sorted(component))

if __name__ == "__main__":
    main()