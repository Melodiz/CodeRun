def find_closest_number_in_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    closest_num = arr[0]
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2
        diff = abs(arr[mid] - target)

        if diff < min_diff:
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
    n = int(input())
    arr = (list(map(int, input().split())))
    k = int(input())
    data = (list(map(int, input().split())))
    # find closes numbers in arr to data
    min_val = float('inf')
    a, b = None, None
    for num in arr:
        best = find_closest_number_in_sorted_array(data, num)
        if abs(best - num) < min_val:
            min_val = abs(best - num)
            a, b = num, best
    print(a, b)

if __name__ == "__main__":
    main()