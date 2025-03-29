def check(a, b, c, d):
    return 3 * d >= 3 * a + b - c

def main():
    a, b, c = [int(input()) for _ in range(3)]
    if a+b+c == 0:
        print(1)
        return
    # using binary search to find the minimum possible value of d such that the average is >= 3.5
    left, right = 0, a+b+c
    while left < right:
        mid = (left + right) // 2
        if check(a, b, c, mid):
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == "__main__":
    main()
