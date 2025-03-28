from typing import List, Tuple
from functools import lru_cache

# Knight's possible moves (half of them are valid in this task)
KNIGHT_MOVES = [(-1, 2), (1, 2), (2, 1), (2, -1)]

def is_valid_move(row: int, col: int, max_row: int, max_col: int) -> bool:
    return 0 <= row < max_row and 0 <= col < max_col

def count_knight_paths(row: int, col: int) -> int:
    if row + col < 5:
        return 0

    @lru_cache(maxsize=None)
    def rec(i: int, j: int) -> int:
        if i == row - 1 and j == col - 1:
            return 1
        
        if i >= row or j >= col:
            return 0
        
        total = 0
        for di, dj in KNIGHT_MOVES:
            new_i, new_j = i + di, j + dj
            if is_valid_move(new_i, new_j, row, col):
                total += rec(new_i, new_j)
        
        return total
    
    return rec(0, 0)

if __name__ == "__main__":
    print(count_knight_paths(*map(int, input().split())))