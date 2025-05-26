from scipy.optimize import curve_fit
import numpy as np


def build_X(x, a, b, c, d):
    tan_x = np.tan(x)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    sqrt_x = np.sqrt(x)
    return a*tan_x + (b*sin_x + c*cos_x)**2 + d*sqrt_x


def read_data():
    n = int(input())
    x, y = [], []
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    return x, y


def main():
    x, y = read_data()
    (a, b, c, d), _ = curve_fit(build_X, np.array(x), np.array(y))
    for coef in (a, b, c, d):
        print(round(abs(coef), 2), end=' ')


if __name__ == "__main__":
    main()
