# Solution for https://coderun.yandex.ru/problem/air-baloons-show
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    dp = [[(1, 1) for _ in range(N)] for _ in range(N)]

    cells = []
    for r in range(N):
        for c in range(N):
            cells.append((grid[r][c], r, c))
    
    cells.sort()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for color, r, c in cells:
        current_len, current_count = dp[r][c]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                neighbor_color = grid[nr][nc]

                if neighbor_color < color:
                    prev_len, prev_count = dp[nr][nc]

                    if prev_len + 1 > current_len:
                        current_len = prev_len + 1
                        current_count = prev_count
                    elif prev_len + 1 == current_len:
                        current_count += prev_count
        
        dp[r][c] = (current_len, current_count)

    max_overall_length = 0
    total_overall_count = 0

    for r in range(N):
        for c in range(N):
            if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                length, count = dp[r][c]
                if length > max_overall_length:
                    max_overall_length = length
                    total_overall_count = count
                elif length == max_overall_length:
                    total_overall_count += count

    print(max_overall_length, total_overall_count)

if __name__ == "__main__":
    main()