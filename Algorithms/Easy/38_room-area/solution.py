def explore_room(grid, start_row, start_col, max_row, max_col):
    if grid[start_row][start_col] == '1' or grid[start_row][start_col] == '*':
        return

    stack = [(start_row, start_col)]
    while stack:
        row, col = stack.pop()
        if row < 0 or row >= max_row or col < 0 or col >= max_col:
            continue
        if grid[row][col] == '1' or grid[row][col] == '*':
            continue

        grid[row][col] = '1'  # Mark the cell as visited

        # Add neighboring cells to the stack
        stack.append((row - 1, col))  # Move up
        stack.append((row + 1, col))  # Move down
        stack.append((row, col - 1))  # Move left
        stack.append((row, col + 1))  # Move right


def main():
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    start_row, start_col = map(int, input()).split()
    max_row, max_col = len(grid), len(grid[0])

    explore_room(grid, start_row - 1, start_col - 1, max_row, max_col)
    print(sum(row.count('1') for row in grid))


if __name__ == "__main__":
    main()