def main():
    a, b  = map(int, input().split())
    cond = input()
    if cond == 'freeze': print(min(a, b))
    elif cond == 'heat': print(max(a, b))
    elif cond == 'auto': print(b)
    else: print(a)

if __name__ == "__main__":
    main()