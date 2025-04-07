def solve_system_of_equations(a, b, c, d, e, f):
    delta = a*d-b*c
    dx = e*d-b*f
    dy = a*f-e*c
    
    if delta != 0:
        return (2, dx/delta, dy/delta)
    else:
        if dx == 0 and dy == 0: 
            # Both equations represent the same line or are both satisfied by any point
            if a == 0 and b == 0 and c == 0 and d == 0:
                if e == 0 and f == 0:
                    return (5, None, None)  # Any pair is a solution
                else:
                    return (0, None, None)  # No solutions
            
            # Check for vertical line (x = constant)
            if b == 0 and d == 0:
                if a != 0:
                    return (3, e/a, None)  # x = e/a, y any
                elif c != 0:
                    return (3, f/c, None)  # x = f/c, y any
            
            # Check for horizontal line (y = constant)
            if a == 0 and c == 0:
                if b != 0:
                    return (4, e/b, None)  # y = e/b, x any
                elif d != 0:
                    return (4, f/d, None)  # y = f/d, x any
            
            # General case: line y = kx + b
            if b != 0:
                return (1, -a/b, e/b)  # y = (-a/b)x + (e/b)
            elif d != 0:
                return (1, -c/d, f/d)  # y = (-c/d)x + (f/d)
            
        # If dx != 0 or dy != 0, the system has no solutions
        return (0, None, None)
    
def main():
    a, b, c, d, e, f = [float(input()) for _ in range(6)]
    flag, x0, y0 = solve_system_of_equations(a, b, c, d, e, f)
    
    if flag == 0 or flag == 5:
        print(flag)
    elif flag == 1 or flag == 2:
        print(flag, x0, y0)
    elif flag == 3:
        print(flag, x0)
    else:  # flag == 4
        print(flag, x0)  # x0 is actually y0 in this case

if __name__ == "__main__":
    main()