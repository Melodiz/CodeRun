def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    df = {}
    l, r = 0, 0
    min_length = float('inf')
    min_ind = (0, 0)
    unique_count = 0
    
    while r < n:
        if arr[r] not in df:
            df[arr[r]] = 0
        if df[arr[r]] == 0:
            unique_count += 1
        df[arr[r]] += 1
        
        while unique_count == k:
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_ind = (l+1, r+1)
            df[arr[l]] -= 1
            if df[arr[l]] == 0:
                unique_count -= 1
            l += 1
        r += 1
    
    print(*min_ind)


if __name__ == "__main__":
    main()