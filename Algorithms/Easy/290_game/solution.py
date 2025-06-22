# Solution for https://coderun.yandex.ru/problem/game
# Other solutions: https://github.com/Melodiz/CodeRun

def update(grid):
    result = [[list(cell) for cell in row] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cnt_stable = 0
            cnt_stable += 1 if i > 0 and grid[i-1][j][1] == 2 else 0
            cnt_stable += 1 if i < len(grid) - 1 and grid[i+1][j][1] == 2 else 0
            cnt_stable += 1 if j > 0 and grid[i][j-1][1] == 2 else 0
            cnt_stable += 1 if j < len(grid[i]) - 1 and grid[i][j+1][1] == 2 else 0
            if cnt_stable > 1:
                result[i][j][1] = 2
            else:
                cnt_active = 0
                cnt_active += 1 if i > 0 and grid[i-1][j][1] == 3 else 0
                cnt_active += 1 if i < len(grid) - 1 and grid[i+1][j][1] == 3 else 0
                cnt_active += 1 if j > 0 and grid[i][j-1][1] == 3 else 0
                cnt_active += 1 if j < len(grid[i]) - 1 and grid[i][j+1][1] == 3 else 0
                if cnt_active > 0 or cnt_stable > 0:
                    result[i][j][1] = 3
                else:
                    result[i][j][1] = 1
            if result[i][j][1] != grid[i][j][1]:
                result[i][j][0] += 1
    return result


def main():
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append([[0, x] for x in list(map(int, input().split()))])
    for _ in range(k):
        grid = update(grid)
    for row in grid:
        print(*[x[0] for x in row])


if __name__ == "__main__":
    main()
