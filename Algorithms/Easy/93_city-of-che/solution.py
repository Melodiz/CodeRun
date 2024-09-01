def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0 
    left, right = 0, 0
    while right < n:
        if arr[right] - arr[left] > k:
            ans += n - right
            left += 1
        else:
            right += 1
    print(ans)


if __name__ == "__main__":
    main()

