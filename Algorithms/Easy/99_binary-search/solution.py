def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 'YES'
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "NO"


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    K = list(map(int, input().split()))
    for num in K:
        print(binary_search(arr, num))


if __name__ == "__main__":
    main()
    
