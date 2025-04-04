def main():
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    probability_of_error = 0.0
    for a, b in nums:
        probability_of_error += a*b
    for a, b in nums:
        print(a*b/probability_of_error)
    return 0

if __name__ == "__main__":
    main()