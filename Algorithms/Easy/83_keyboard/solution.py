def main():
    k = int(input())
    limits = list(map(int, input().split()))
    n = int(input())
    keys = list(map(int, input().split()))
    from collections import Counter
    c = Counter(keys)
    for i in range(k):
        if limits[i] >= c[i+1]:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()