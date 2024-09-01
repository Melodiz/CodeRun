import math
from collections import deque

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def can_assign_all_users(users, points, max_distance):
    n = len(users)
    m = len(points)
    
    # Create adjacency list for bipartite graph
    adj = [[] for _ in range(n + m + 2)]
    source = n + m
    sink = n + m + 1
    
    for i in range(n):
        adj[source].append((i, 1))  # Source to user
        adj[i].append((source, 0))  # Reverse edge with capacity 0
    
    for j in range(m):
        adj[n + j].append((sink, points[j][2]))  # Point to sink with capacity a_j
        adj[sink].append((n + j, 0))  # Reverse edge with capacity 0
    
    for i in range(n):
        for j in range(m):
            if distance(users[i][0], users[i][1], points[j][0], points[j][1]) <= max_distance:
                adj[i].append((n + j, 1))  # User to point
                adj[n + j].append((i, 0))  # Reverse edge with capacity 0
    
    # Implementing BFS for finding augmenting path
    def bfs():
        parent = [-1] * (n + m + 2)
        parent[source] = -2
        queue = deque([(source, float('inf'))])
        
        while queue:
            current, flow = queue.popleft()
            
            for neighbor, capacity in adj[current]:
                if parent[neighbor] == -1 and capacity > 0:
                    parent[neighbor] = current
                    new_flow = min(flow, capacity)
                    if neighbor == sink:
                        return new_flow, parent
                    queue.append((neighbor, new_flow))
        
        return 0, parent
    
    # Implementing Edmonds-Karp algorithm for max-flow
    max_flow = 0
    while True:
        flow, parent = bfs()
        if flow == 0:
            break
        max_flow += flow
        current = sink
        while current != source:
            prev = parent[current]
            for i in range(len(adj[prev])):
                if adj[prev][i][0] == current:
                    adj[prev][i] = (current, adj[prev][i][1] - flow)
            for i in range(len(adj[current])):
                if adj[current][i][0] == prev:
                    adj[current][i] = (prev, adj[current][i][1] + flow)
            current = prev
    
    return max_flow == n

def find_min_max_distance(n, m, users, points):
    left, right = 0, 1e9
    while right - left > 1e-6:
        mid = (left + right) / 2
        if can_assign_all_users(users, points, mid):
            right = mid
        else:
            left = mid
    return right

# Reading input
n, m = map(int, input().split())
users = [tuple(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(m)]

# Finding the minimum maximum distance
result = find_min_max_distance(n, m, users, points)
print(f"{result:.10f}")