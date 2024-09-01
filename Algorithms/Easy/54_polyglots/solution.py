def main():
    n = int(input())

    common = set()
    result = set()
    # first child
    k = int(input())
    new = set([input() for _ in range(k)])
    common.update(new)
    result.update(new)
    # rest
    for _ in range(n-1):
        k = int(input())
        new = set([input() for _ in range(k)])
        common.intersection_update(new)
        result.update(new)
    print(len(common))
    print('\n'.join(common))
    print(len(result))
    print('\n'.join(result))


if __name__ == "__main__":
    main()
