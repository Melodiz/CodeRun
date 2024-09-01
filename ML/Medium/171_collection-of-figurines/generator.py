import random
from collections import deque
import math
import time


def correct_solution(n, k, arr):
    needed_set = set(range(1, k + 1))
    cur_sum = 0
    min_sum = math.inf
    deq = deque()
    dct = {}

    for i in arr:
        if len(dct) < k:
            cur_sum += i
            deq.append(i)
            if i in needed_set:
                dct[i] = dct.get(i, 0) + 1
            if len(dct) == k:
                while True:
                    cur = deq[0]
                    if cur not in dct or dct[cur] > 1:
                        deq.popleft()
                        cur_sum -= cur
                        if cur in dct:
                            dct[cur] -= 1
                    else:
                        break
        else:
            if i in needed_set:
                cur_sum += i
                deq.append(i)
                dct[i] = dct.get(i, 0) + 1
                while deq:
                    cur = deq[0]
                    if cur not in dct or dct[cur] > 1:
                        deq.popleft()
                        cur_sum -= cur
                        if cur in dct:
                            dct[cur] -= 1
                    else:
                        break
            else:
                cur_sum += i
                deq.append(i)
        if cur_sum < min_sum and len(dct) == k:
            min_sum = cur_sum

    return min_sum


def my_solution(n, k, data):

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
            break
    return min_sum

def generate_test_case():
    n = random.randint(1, 30)
    k = random.randint(1, n)
    arr = list(range(1, k + 1))
    while len(arr) < n:
        arr.append(random.randint(1, k))
    random.shuffle(arr)
    return n, k, arr


def write_to_file(n, k, arr):
    with open("input.txt", "w") as file:
        file.write(f"{n} {k}\n")
        file.write(" ".join(map(str, arr)) + "\n")


def main():
    count = 0
    while count < 1_000_000:
        n, k, arr = generate_test_case()
        result_correct = correct_solution(n, k, arr)
        result_my = my_solution(n, k, arr)
        if result_correct != result_my:
            write_to_file(n, k, arr)
            print(f"Discrepancy found!\nInput written to input.txt\nn={\
                  n}, k={k}, arr={arr}")
            print(f"correct_solution: {\
                  result_correct}, my_solution: {result_my}")
            break
        count += 1
    print(f"No discrepancy found after 1,000,000 iterations.")


if __name__ == "__main__":
    main()
