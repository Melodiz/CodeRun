def main():
    nums = [int(input()) for _ in range(5)]
    a, b = sorted(nums[:3])[:2]
    d, e = sorted(nums[3:])[:2]
    if a <= d and b <= e: print("YES")
    else: print("NO")

if __name__ == "__main__":
    main()