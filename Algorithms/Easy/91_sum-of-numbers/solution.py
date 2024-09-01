def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = 0
    l = 0
    current_sum = 0
    
    for r in range(n):
        current_sum += arr[r]
        while current_sum > k and l <= r:
            current_sum -= arr[l]
            l += 1
        if current_sum == k:
            counter += 1
    
    print(counter)

if __name__ == "__main__":
    main()

# hash map approach for O(n) time complexity
# def main():
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     counter = 0
#     current_sum = 0
#     prefix_sums = {0: 1}
    
#     for num in arr:
#         current_sum += num
#         if current_sum - k in prefix_sums:
#             counter += prefix_sums[current_sum - k]
#         if current_sum in prefix_sums:
#             prefix_sums[current_sum] += 1
#         else:
#             prefix_sums[current_sum] = 1
    
#     print(counter)

# if __name__ == "__main__":
#     main()