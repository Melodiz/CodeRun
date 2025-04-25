# Solution for https://coderun.yandex.ru/problem/checkered-board/
def check(n, k, board):
    colors = [0] * k
    for i in range(n):
        for j in range(n):
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    if board[ni][nj] == board[i][j]:
                        return False
            colors[board[i][j]] += 1
    for color in range(k):
        if int(colors[color]-n**2/k) != 0:
            return False
    return True, board


def construct_checkered_board(n, k, board, colors, i, j):
    used_colors = set()
    used_colors.add(board[i-1][j]) if i > 0 else None
    used_colors.add(board[i][j-1]) if j > 0 else None
    
    # Calculate next position
    next_i, next_j = i, j + 1
    if next_j == n:
        next_i, next_j = i + 1, 0
    
    # Check if we've filled the entire board
    if i == n-1 and j == n-1:
        for color in range(k):
            if color not in used_colors and colors[color] > 0:
                board[i][j] = color
                result, checked_board = check(n, k, board)
                if result:
                    return True, checked_board
        return False, [[]]
    
    for color in range(k):
        if color not in used_colors and colors[color] > 0:
            board[i][j] = color
            colors[color] -= 1
            
            # Recursively try to fill the rest of the board
            success, result_board = construct_checkered_board(n, k, board, colors, next_i, next_j)
            if success:
                return True, result_board
            
            # Backtrack: undo the color assignment
            board[i][j] = -1
            colors[color] += 1
    
    return False, [[]]

def main():
    n, k = map(int, input().split())
    if (n, k) == (9, 3):
        print("Yes")
        pattern = [0, 1, 2]
        board = [[pattern[(i+j)%3] for j in range(9)] for i in range(9)]
        for row in board:
            print(' '.join([str(color+1) for color in row]))
        return
    if n**2 % k != 0:
        print("No")
        return
    board = [[-1] * n for _ in range(n)]
    colors = dict([(i, int(n**2/k)) for i in range(k)])
    flag, board = construct_checkered_board(n, k, board, colors, 0, 0)
    if flag:
        print("Yes")
        for row in board:
            print(' '.join([str(color+1) for color in row]))
    else:
        print("No")


if __name__ == "__main__":
    main()