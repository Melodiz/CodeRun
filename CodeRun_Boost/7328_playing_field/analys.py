def compute_dificulty(grid):
    ans = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            # count the number of 1s in the neighboring cells
            if grid[i][j] == 1:
                continue
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        count += grid[ni][nj]
            ans += count
    return ans

def brute(n):
    # generate all possible nxn grids with 0s and 1s
    max_value = 0
    ans_grids= []
    from itertools import product
    grids = product([0, 1], repeat=n * n)
    for grid in grids:
        grid = [list(grid[i:i + n]) for i in range(0, len(grid), n)]
        difficulty = compute_dificulty(grid)
        if difficulty > max_value:
            max_value = difficulty
            ans_grids = [grid]
            for row in grid:
                print(''.join(['x' if cell == 1 else '.' for cell in row]))
                print()
        elif difficulty == max_value:
            ans_grids.append(grid)
    return max_value, ans_grids



if __name__ == "__main__":
    n = 4  # Example size of the grid
    max_difficulty, grids = brute(n)
    print(f"Maximum difficulty: {max_difficulty}")
    print(f"Grids with maximum difficulty: {len(grids)}")
    for grid in grids:
        for row in grid:
            print(''.join(['x' if cell == 1 else '.' for cell in row]))
        print("---")