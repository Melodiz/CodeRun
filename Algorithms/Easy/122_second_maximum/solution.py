def main():
    arr = list(map(int, input().split()))[:-1]
    max_val, second_max_val = float('-inf'), float('-inf')
    for num in arr:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val and num != max_val:
            second_max_val = num

    print(second_max_val)


if __name__ == "__main__":
    main()