def find_cycle(graph):
    n = len(graph)
    visited = [False] * n
    path = []
    
    def dfs(node, parent):
        visited[node] = True
        path.append(node)
        
        for neighbor in range(n):
            if graph[node][neighbor] == 1:  # If there's an edge
                if not visited[neighbor]:
                    cycle = dfs(neighbor, node)
                    if cycle:
                        return cycle
                elif neighbor != parent:
                    # Cycle detected
                    cycle_start = path.index(neighbor)
                    return path[cycle_start:] + [neighbor]
        
        path.pop()
        return None

    for node in range(n):
        if not visited[node]:
            cycle = dfs(node, -1)
            if cycle:
                return cycle
    
    return None

def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cycle = find_cycle(graph)
    if cycle:
        print('YES')
        print(len(cycle)-1)
        for node in cycle[:-1]:
            print(node+1, end=' ')
    else:
        print('NO')

if __name__ == '__main__':
    main()