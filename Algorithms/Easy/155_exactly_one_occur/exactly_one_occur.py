from collections import Counter

def main():
    n = int(input())
    data = Counter(map(int, input().split()))
    print(sum(1 for v in data.values() if v == 1))


if __name__ == "__main__":
    main()