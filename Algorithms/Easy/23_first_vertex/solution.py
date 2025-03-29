def find_reachable_vertices(n, edges):
    from collections import defaultdict, deque

    # Построение обратного графа
    reverse_graph = defaultdict(list)
    for u, v in edges:
        reverse_graph[v].append(u)

    # Поиск в ширину (BFS) из первой вершины в обратном графе
    reachable = set()
    queue = deque([1])
    while queue:
        vertex = queue.popleft()
        if vertex not in reachable:
            reachable.add(vertex)
            for neighbor in reverse_graph[vertex]:
                if neighbor not in reachable:
                    queue.append(neighbor)

    # Возвращаем отсортированный список достижимых вершин
    return sorted(reachable)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    reachable_vertices = find_reachable_vertices(n, edges)
    print(" ".join(map(str, reachable_vertices)))

if __name__ == "__main__":
    main()