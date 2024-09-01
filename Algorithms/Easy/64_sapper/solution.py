def main():
    n, m, k = map(int, input().split())
    grid = [[0 for _ in range(m+2)] for t in range(n+2)]
    for t in range(k):
        x, y  = map(int, input().split())
        x, y = x, y
        grid[x][y] = 999
        grid[x-1][y-1] +=1 
        grid[x-1][y] += 1
        grid[x-1][y+1] += 1
        grid[x][y-1] += 1
        grid[x][y+1] += 1
        grid[x+1][y-1] += 1
        grid[x+1][y] += 1
        grid[x+1][y+1] += 1
    # remove the border cells
    grid = grid[1:-1]
    for row in grid:
        ans = [row[x] if row[x] < 100 else '*' for x in range(1, len(row)-1)]
        print(*ans)

if __name__ == "__main__":
    main()