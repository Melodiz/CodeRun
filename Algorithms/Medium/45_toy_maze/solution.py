# Solution for https://coderun.yandex.ru/problem/toy-maze
# Other solutions: https://github.com/Melodiz/CodeRun

from collections import deque

def solve():
    N, M = map(int, input().split())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input().split())))

    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while q:
        r, c, moves = q.popleft()

        new_r, new_c = r, c
        temp_r = r
        while temp_r - 1 >= 0:
            if maze[temp_r - 1][c] == 1:
                break
            temp_r -= 1
            if maze[temp_r][c] == 2:
                print(moves + 1)
                return
            new_r = temp_r
        
        if (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            q.append((new_r, new_c, moves + 1))


        new_r, new_c = r, c
        temp_r = r
        while temp_r + 1 < N:
            if maze[temp_r + 1][c] == 1:
                break
            temp_r += 1
            if maze[temp_r][c] == 2:
                print(moves + 1)
                return
            new_r = temp_r
        if (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            q.append((new_r, new_c, moves + 1))


        new_r, new_c = r, c
        temp_c = c
        while temp_c - 1 >= 0:
            if maze[r][temp_c - 1] == 1:
                break
            temp_c -= 1
            if maze[r][temp_c] == 2:
                print(moves + 1)
                return
            new_c = temp_c
        if (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            q.append((new_r, new_c, moves + 1))


        new_r, new_c = r, c
        temp_c = c
        while temp_c + 1 < M:
            if maze[r][temp_c + 1] == 1:
                break
            temp_c += 1
            if maze[r][temp_c] == 2:
                print(moves + 1)
                return
            new_c = temp_c
        if (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            q.append((new_r, new_c, moves + 1))

if __name__ == "__main__":
    solve()