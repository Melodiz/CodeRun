from collections import deque, defaultdict

def build_graph(lines):
    graph = defaultdict(list)
    station_to_lines = defaultdict(list)
    
    for i, line in enumerate(lines):
        for station in line:
            station_to_lines[station].append(i)
    
    for stations in station_to_lines.values():
        for i in range(len(stations)):
            for j in range(i + 1, len(stations)):
                graph[stations[i]].append(stations[j])
                graph[stations[j]].append(stations[i])
    
    return graph, station_to_lines

def bfs(graph, start_lines, end_lines):
    queue = deque([(line, 0) for line in start_lines])
    visited = set(start_lines)
    
    while queue:
        current_line, transfers = queue.popleft()
        
        if current_line in end_lines:
            return transfers
        
        for neighbor in graph[current_line]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, transfers + 1))
    
    return -1

def min_transfers(n, m, lines, A, B):
    graph, station_to_lines = build_graph(lines)
    
    start_lines = station_to_lines[A]
    end_lines = station_to_lines[B]
    
    if not start_lines or not end_lines:
        return -1
    
    return bfs(graph, start_lines, end_lines)

def main():
    n = int(input())
    m = int(input())
    lines = []
    
    for _ in range(m):
        line = list(map(int, input().split()))[1:]
        lines.append(line)
    
    A, B = map(int, input().split())
    
    result = min_transfers(n, m, lines, A, B)
    print(result)

if __name__ == "__main__":
    main()