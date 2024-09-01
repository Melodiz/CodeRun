def main():
    n = int(input())
    data = [input().split()[0] for _ in range(n)]
    print(len(set(data)))


if __name__ == "__main__":
    main()
