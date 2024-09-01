def check(k, l, arr):
    for el in arr:
        k -= (el // l)
    return k <= 0

def binary_search_max(k, arr):
    if k > sum(arr): return 0
    left, right = 1, max(arr)
    while left < right:
        mid = (left + right + 1) // 2
        if check(k, mid, arr):
            left = mid
        else:
            right = mid - 1
    return left

def main():
    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    print(binary_search_max(k, arr))

if __name__ == "__main__":
    main()