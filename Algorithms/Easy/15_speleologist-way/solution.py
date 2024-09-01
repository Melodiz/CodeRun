from collections import deque
def reverse_maze_walk(maze, n):
    queue = deque()
    for i in range(n):
        for j in range(n):
            if maze[0][i][j] == '.':
                queue.append((0, i, j, 0))
                maze[0][i][j] = '#'

    directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0),
                  (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    while queue:
        layer, x, y, steps = queue.popleft()
        for dl, dx, dy in directions:
            nl, nx, ny = layer + dl, x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and 0 <= nl < n:
                if maze[nl][nx][ny] == '.':
                    queue.append((nl, nx, ny, steps + 1))
                    maze[nl][nx][ny] = '#'
                elif maze[nl][nx][ny] == 'S':
                    return steps + 1
    return -1


def main():
    n = int(input())
    maze = []
    for _ in range(n):
        input()
        block = []
        for t in range(n):
            block.append(list(input().strip()))
        maze.append(block)
    print(reverse_maze_walk(maze, n))

if __name__ == "__main__":
    main()
