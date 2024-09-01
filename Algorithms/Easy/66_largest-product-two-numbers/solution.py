def max_product_two(arr):

    min_a, min_b = float('inf'), float('inf')
    max_a, max_b = float('-inf'), float('-inf')

    for el in arr:
        if el < min_a:
            min_a, min_b = el, min_a
        elif el < min_b:
            min_b = el

        if el > max_a:
            max_a, max_b = el, max_a
        elif el > max_b:
            max_b = el

    p1 = min_a * min_b
    p2 = max_a * max_b

    return (min_a, min_b) if p1 > p2 else (max_a, max_b)

def main():
    arr = list(map(int, input().split()))
    print(*sorted(max_product_two(arr)))

if __name__ == "__main__":
    main()