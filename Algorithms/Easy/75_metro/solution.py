def main():
    a, b = int(input()), int(input())
    n, m = int(input()), int(input())
    min_a = (a+1)*(n-1)+1
    max_a = (a+1)*(n)+a
    min_b = (b+1)*(m-1)+1
    max_b = (b+1)*(m)+b
    if max_a < min_b or max_b < min_a: print(-1)
    else: print(max(min_a, min_b), min(max_a, max_b))

if __name__ == "__main__":
    main()