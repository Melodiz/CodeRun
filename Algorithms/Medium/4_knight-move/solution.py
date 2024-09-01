from functools import lru_cache

@lru_cache(maxsize=None)
def rec(i, j, goala, goalb):
    if i == goala and j == goalb:
        return 1
    if i > goala or j > goalb:
        return 0
    return rec(i+2, j+1, goala, goalb) + rec(i+1, j+2, goala, goalb)

def main():
    n, m = map(int, input().split())
    print(rec(0, 0, n-1, m-1))



if __name__ == "__main__":
    main()