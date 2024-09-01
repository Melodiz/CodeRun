def main():
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    main()