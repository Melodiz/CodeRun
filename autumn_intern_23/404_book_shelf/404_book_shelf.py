import sys
from functools import lru_cache

def main():
    n = int(input())
    books = tuple(map(int, input().split()))  # Convert list to tuple
    print(solver(books, 0, -1, 1000, 0))

@lru_cache(None)
def solver(books, i, left, right, count):
    if i == len(books):
        return count
    
    if books[i] >= left and books[i] <= right:
        return max(
            solver(books, i+1, left, right, count),
            max(
                solver(books, i+1, books[i], right, count+1),
                solver(books, i+1, left, books[i], count+1)
            )
        )
    else:
        return solver(books, i+1, left, right, count)

if __name__ == '__main__':
    main()