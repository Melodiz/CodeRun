def check(n, a, b, w, h):
    # check is it possible to distribute n boxes of size a * b into a room of size w * h
    # such that each box has at least one side parallel to the room's width or height
    return (w // a) * (h // b) >= n or (h // a) * (w // b) >= n

def binary_search_max(n, a, b, w, h):
    # find the maximum possible value of d
    left, right = 0, min(w, h)//2 +1 
    while left < right:
        mid = (left + right + 1) // 2
        if check(n, a+2*mid, b+2*mid, w, h):
            left = mid
        else:
            right = mid - 1
    return left

def main():
    n, a, b, w, h = map(int, input().split())
    print(binary_search_max(n, a, b, w, h))

if __name__ == "__main__":
    main()