def main():
    arr = list(map(int, input().split()))[:-1]
    print(*sorted(set(arr)))


if __name__ == "__main__":
    main()
