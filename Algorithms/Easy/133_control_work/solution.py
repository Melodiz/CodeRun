def main():
    n = int(input())
    k = int(input())
    a0, b0 = int(input()), int(input())
    position = a0 * 2 + b0 - 3
    a1, b1 = (position + k) // 2 + 1, (position + k) % 2 + 1
    a2, b2 = (position - k) // 2 + 1, (position - k) % 2 + 1

    if 0 <= position + k < n and 0 <= position - k < n:
        if abs(a0 - a1) < abs(a0 - a2):
            print(a1, b1)
        elif abs(a0 - a1) > abs(a0 - a2):
            print(a2, b2)
        else:
            print(a1, b1)
    elif 0 <= position + k < n:
        print(a1, b1)
    elif 0 <= position - k < n:
        print(a2, b2)
    else:
        print(-1)

if __name__ == "__main__":
    main()