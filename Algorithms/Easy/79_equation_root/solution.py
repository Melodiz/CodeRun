def main():
    a, b, c = [int(input()) for _ in range(3)]
    if a == 0 and b == c**2: print("MANY SOLUTIONS")
    elif a == 0 or c < 0: print("NO SOLUTION")
    else:
        solutions = []
        for x in range(-101, 101):
            if a*x+b == c**2: solutions.append(x)
        if len(solutions) == 0: print("NO SOLUTION")
        else: print(*sorted(solutions))


if __name__ == "__main__":
    main()