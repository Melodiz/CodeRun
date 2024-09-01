def build_board_knight(letter, num):
    board = [[-1 for _ in range(8)] for t in range(8)]
    y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(letter)
    x = num - 1
    board[x][y] = 0

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    queue = [(x, y, 0)]
    
    while queue:
        cx, cy, dist = queue.pop(0)
        for move in moves:
            nx, ny = cx + move[0], cy + move[1]
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == -1:
                board[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    
    return board
def main():
    a, b = input().split()
    board_1 = build_board_knight(a[0], int(a[1]))
    board_2 = build_board_knight(b[0], int(b[1]))
    candidates = set()
    for i in range(8):
        for j in range(8):
            if board_1[i][j] != -1 and board_2[i][j] == board_1[i][j]:
                candidates.add(board_1[i][j])
    if len(candidates) == 0:
        print(-1)
    else:
        print(min(candidates))


if __name__ == "__main__":
    main()
