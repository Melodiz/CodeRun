def check(a, b, w, n):
    return 2*w*(a+b - 2*w) <= n

def binary_search_max(a, b, n):
    # find maximum w such that check(a, b, w, n) is true
    left, right = 0, min(a, b) // 2
    while left < right:
        mid = (left + right + 1) // 2
        if check(a, b, mid, n):
            left = mid
        else:
            right = mid - 1
    return left

def main():
    a, b, n = [int(input()) for _ in range(3)]
    print(binary_search_max(a, b, n))


if __name__ == "__main__":
    main()
