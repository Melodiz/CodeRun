import time


def main():
    # Read data from file
    with open("input.txt", "r") as file:
        n, k = map(int, file.readline().split())
        data = list(map(int, file.readline().split()))

    dp = [0] * k
    min_sum = float('inf')
    l, r = 0, 0
    current_sum = 0
    unique_count = 0

    while r < n:
        if unique_count == k:
            l += 1
            min_sum = min(min_sum, current_sum)
            if data[l] - 1 < k:
                dp[data[l] - 1] -= 1
                if dp[data[l] - 1] == 0:
                    unique_count -= 1
            current_sum -= data[l]
        else:
            if data[r] - 1 < k:
                if dp[data[r] - 1] == 0:
                    unique_count += 1
                dp[data[r] - 1] += 1
            current_sum += data[r]
            r += 1

    if unique_count == k:
        min_sum = min(min_sum, current_sum)

    print(min_sum)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    # Expected output: 75003509803
    
