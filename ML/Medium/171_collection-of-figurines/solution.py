def main():
    # Read data from file
    with open("input.txt", "r") as file:
        n, k = map(int, file.readline().split())  # Read n and k from the first line
        data = list(map(int, file.readline().split()))  # Read the array of integers from the second line

    dp = [0] * k  # Initialize a list to keep track of counts of each unique number
    min_sum = float('inf')  # Initialize the minimum sum to infinity
    l, r = 0, 0  # Initialize left and right pointers
    current_sum = 0  # Initialize the current sum of the window
    unique_count = 0  # Initialize the count of unique numbers in the window

    # Sliding window approach
    while r < n:
        if unique_count == k:  # If we have k unique numbers in the window
            min_sum = min(min_sum, current_sum)  # Update the minimum sum
            if data[l] - 1 < k:  # If the leftmost number is within the range
                dp[data[l] - 1] -= 1  # Decrease its count
                if dp[data[l] - 1] == 0:  # If its count becomes zero
                    unique_count -= 1  # Decrease the unique count
            current_sum -= data[l]  # Subtract the leftmost number from the current sum
            l += 1  # Move the left pointer to the right
        else:
            if data[r] - 1 < k:  # If the rightmost number is within the range
                if dp[data[r] - 1] == 0:  # If its count is zero
                    unique_count += 1  # Increase the unique count
                dp[data[r] - 1] += 1  # Increase its count
            current_sum += data[r]  # Add the rightmost number to the current sum
            r += 1  # Move the right pointer to the right

    # Final check for the remaining window
    while l < n:
        if unique_count == k:  # If we have k unique numbers in the window
            min_sum = min(min_sum, current_sum)  # Update the minimum sum
            if data[l] - 1 < k:  # If the leftmost number is within the range
                dp[data[l] - 1] -= 1  # Decrease its count
                if dp[data[l] - 1] == 0:  # If its count becomes zero
                    unique_count -= 1  # Decrease the unique count
            current_sum -= data[l]  # Subtract the leftmost number from the current sum
            l += 1  # Move the left pointer to the right
        else: 
            break  # Break if we don't have k unique numbers

    print(min_sum)  # Print the minimum sum


if __name__ == '__main__':
    main()