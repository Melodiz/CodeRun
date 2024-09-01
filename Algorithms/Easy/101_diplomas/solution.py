def check(a, b, k,  c):
    return ((c // a) * (c // b)) >= k


def binary_search(a, b, k):
    left = 0; right = a*b*k
    # find the smallest c in range such that (c // a * c // b) >= k
    while left < right:
        mid = (left + right) // 2
        if check(a, b, k, mid):
            right = mid
        else:
            left = mid + 1
    return left 

def main():
    a, b, k = map(int, input().split())
    print(binary_search(a, b, k))


if __name__ == "__main__":
    main()
    