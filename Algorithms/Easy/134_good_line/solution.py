def main():
    n = int(input())
    ans = 0
    data = [int(input()) for _ in range(n)]
    for i in range(n-1):
        ans += min(data[i], data[i+1])
        # data[i+1] -= min(data[i], data[i+1])
    print(ans)


if __name__ == "__main__":
    main()
