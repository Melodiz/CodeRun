import sys
from scipy.optimize import minimize

def query(x0):
    x, y = x0
    print(x, y)
    sys.stdout.flush()
    response = input().strip().split()
    if response[0] == '+':
        sys.exit(0)
    return -float(response[1])

def main():
    bounds = [(-50, 100), (-50, 100)]
    x, y, f = map(float, input().split())
    res = minimize(query, [x, y], method='trust-constr', bounds=bounds)

if __name__ == "__main__":
    main()