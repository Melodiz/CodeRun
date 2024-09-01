def find_closest_number_binary(arr, target):
    left, right = 0, len(arr) - 1
    closest_num = arr[0]
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2
        diff = abs(arr[mid] - target)

        if diff < min_diff or (diff == min_diff and arr[mid] < closest_num):
            min_diff = diff
            closest_num = arr[mid]

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]

    return closest_num


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    K = list(map(int, input().split()))
    for num in K:
        print(find_closest_number_binary(arr, num))


if __name__ == "__main__":
    main()
    

