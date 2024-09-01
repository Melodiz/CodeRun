def main():
    given = set(map(int, input().split()))
    req = set(map(int, list(input())))
    print(len(req - given))


if __name__ == "__main__":
    main()