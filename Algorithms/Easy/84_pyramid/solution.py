def main():
    n = int(input())
    data = {}
    for _ in range(n):
        a, b = map(int, input().split())
        data[a] = max(data.get(a, 0), b)
    print(sum(data.values()))

if __name__ == "__main__":
    main()
