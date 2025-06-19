# Solution for https://coderun.yandex.ru/problem/tic-tac-toe
# Other solutions: https://github.com/Melodiz/CodeRun

def check_winner(board):
    # try to find 5 '0' or 'X' in a row/column/diagonal
    n, m = len(board), len(board[0])    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                if i + 4 < n and board[i+1][j] == 'O' and board[i+2][j] == 'O' and board[i+3][j] == 'O' and board[i+4][j] == 'O':
                    return 'Yes'
                if j + 4 < m and board[i][j+1] == 'O' and board[i][j+2] == 'O' and board[i][j+3] == 'O' and board[i][j+4] == 'O':
                    return 'Yes'
                if i + 4 < n and j + 4 < m and board[i+1][j+1] == 'O' and board[i+2][j+2] == 'O' and board[i+3][j+3] == 'O' and board[i+4][j+4] == 'O':
                    return 'Yes'
                if i + 4 < n and j - 4 >= 0 and board[i+1][j-1] == 'O' and board[i+2][j-2] == 'O' and board[i+3][j-3] == 'O' and board[i+4][j-4] == 'O':
                    return 'Yes'
            elif board[i][j] == 'X':
                if i + 4 < n and board[i+1][j] == 'X' and board[i+2][j] == 'X' and board[i+3][j] == 'X' and board[i+4][j] == 'X':
                    return 'Yes'
                if j + 4 < m and board[i][j+1] == 'X' and board[i][j+2] == 'X' and board[i][j+3] == 'X' and board[i][j+4] == 'X':
                    return 'Yes'
                if i + 4 < n and j + 4 < m and board[i+1][j+1] == 'X' and board[i+2][j+2] == 'X' and board[i+3][j+3] == 'X' and board[i+4][j+4] == 'X':
                    return 'Yes'
                if i + 4 < n and j - 4 >= 0 and board[i+1][j-1] == 'X' and board[i+2][j-2] == 'X' and board[i+3][j-3] == 'X' and board[i+4][j-4] == 'X':
                    return 'Yes'
    return 'No'

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    print(check_winner(board))

if __name__ == "__main__":
    main()
