def main():
    n, k, m = map(int, input().split())
    if k < m:
        print(0)
        return
    ans = 0
    det_in_zag = k // m
    rest_in_zag = k - det_in_zag * m
    while n >= k:
        kolvo_zag = n // k
        n -= kolvo_zag * k
        ans += kolvo_zag * det_in_zag
        n += kolvo_zag * rest_in_zag
    print(ans)


if __name__ == "__main__":
    main()
