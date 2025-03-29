def some_func(arr: list[int], k: int) -> int:
    # arr: sorted list of unique integers
    # k: plank value
    # return the number of elements in arr that are less than k
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    n = int(input())
    arr = sorted(set(map(int, input().split())))

    k = int(input())
    collectors = list(map(int, input().split()))
    for collector in collectors:
        print(some_func(arr, collector))

if __name__ == "__main__":
    main()