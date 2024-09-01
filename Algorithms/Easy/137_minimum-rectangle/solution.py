def main():
    n = int(input())
    x, y = [], []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    left_x = min(x)
    right_x = max(x)
    top_y = max(y)
    bottom_y = min(y)
    print(left_x, bottom_y, right_x, top_y)


if __name__ == "__main__":
    main()
