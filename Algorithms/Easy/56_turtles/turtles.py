def max_truthful_turtles(n, statements):
    table = [0]*n
    for above, below in statements:
        if above + below == n - 1 and 0 <= above < n and 0 <= below < n and not table[above]:
            table[above] = True
    return sum(table)

if __name__ == "__main__":
    n = int(input())
    statements = []
    for _ in range(n):
        in_front, back = map(int, input().split())
        statements.append((in_front, back))
    print(max_truthful_turtles(n, statements))