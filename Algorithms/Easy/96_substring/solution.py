def max_subarray_sum_with_k_presses(arr, k, n):
    max_length = 0
    l = 0
    count = {}
    index = (0, 0)

    for r in range(n):
        if arr[r] not in count:
            count[arr[r]] = 0
        count[arr[r]] += 1

        while count[arr[r]] > k:
            count[arr[l]] -= 1
            l += 1
        if r - l + 1 > max_length:  
            max_length = r - l + 1
            index = (max_length, l+1)

    return index


def main():
    n, k = map(int, input().split())
    arr = input()
    # find the maximum subarray s.t. every element presses no more than k times
    max_subarray_sum = max_subarray_sum_with_k_presses(arr, k, n)
    print(*max_subarray_sum)


if __name__ == "__main__":
    main()
