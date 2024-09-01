def max_product_of_three(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

def main():
    nums = list(map(int, input().split()))
    result = max_product_of_three(nums)
    print(result)

if __name__ == "__main__":
    main()