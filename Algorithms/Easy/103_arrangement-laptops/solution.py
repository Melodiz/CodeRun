def main():
    a, b, c, d = map(int, input().split())
    vars = sorted([[max(a, c) * (b + d), max(a, c), b+d],
         [max(a, d) * (b + c), max(a, d), b+c],
         [max(b, c) * (a + d), max(b, c), a+d],
         [max(b, d) * (a + c), max(b, d), a+c]])
    print(vars[0][1], vars[0][2])


if __name__ == "__main__":
    main()