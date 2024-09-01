def main():
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    print(*sorted(set_a.intersection(set_b)))

if __name__ == "__main__":
    main()