from collections import deque

def is_valid(x, y, N, M):
    return 1 <= x <= N and 1 <= y <= M

def bfs(N, M, start_x, start_y):
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    dist = [[-1] * (M + 1) for _ in range(N + 1)]
    queue = deque([(start_x, start_y)])
    dist[start_x][start_y] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, N, M) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    return dist

def min_sum_of_paths(N, M, S, T, fleas):
    dist = bfs(N, M, S, T)
    total_distance = 0
    
    for x, y in fleas:
        if dist[x][y] == -1:
            return -1
        total_distance += dist[x][y]
    
    return total_distance

def main():
    N, M, S, T, Q = map(int, input().split())
    fleas = [list(map(int, input().split())) for _ in range(Q)]

    result = min_sum_of_paths(N, M, S, T, fleas)
    print(result)

if __name__ == "__main__":
    main()