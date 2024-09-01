def main():
    n = int(input())
    df = {}
    for _ in range(n):
        a, b = input().split()
        df[a] = b
    goal = input()
    for key, value in df.items():
        if key == goal:
            print(value)
            return
        if value == goal:
            print(key)
            return
    print(-1)


if __name__ == "__main__":
    main()
