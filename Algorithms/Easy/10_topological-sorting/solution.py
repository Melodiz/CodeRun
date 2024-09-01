from collections import deque, defaultdict

def topological_sort(n, edges):
    # Initialize the graph and in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and compute in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Initialize the queue with vertices of zero in-degree
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycles
    if len(topo_order) == n:
        return topo_order
    else:
        return -1

def main():
    # Read input data
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    # Get the topological sort
    result = topological_sort(n, edges)

    # Print the result
    if result == -1:
        print(result)
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()