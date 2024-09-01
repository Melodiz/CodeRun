def min_time_to_copy(n, x, y):
    if n == 1:
        return min(x, y)
    
    left, right = 0, min(x, y) * n
    while left < right:
        mid = (left + right) // 2
        if (mid // x) + (mid // y) >= n - 1:
            right = mid
        else:
            left = mid + 1
    
    return left + min(x, y)

def main():
    n, x, y = map(int, input().split())
    print(min_time_to_copy(n, x, y))

if __name__ == "__main__":
    main()