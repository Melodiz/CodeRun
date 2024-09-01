import sys
import numpy as np


def main():
    n = int(input())
    X = np.zeros(n)
    Y = np.zeros(n)

    unique_values = set()
    sum_total = 0
    arr_index = 0
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if (x, y) not in unique_values:
            sum_total += y
            X[arr_index], Y[arr_index] = x, y
            unique_values.add((x, y))
            arr_index += 1


    X = X[:arr_index]
    Y = Y[:arr_index]

    sort_indices = np.argsort(X)

    X = X[sort_indices]
    Y = Y[sort_indices]

    best_threshold, best_rmse = None, float('-inf')
    prev_threshold = None

    flag = True
    if len(set(X)) == 1 or len(set(Y)) == 1:
        flag = False
    else:
        sum_left_cs = np.cumsum(Y)

    if flag:
        n = len(X)
        for i in range(1, n):
            threshold = (X[i-1] + X[i]) / 2

            if X[i-1] >= threshold:
                continue

            sum_left = sum_left_cs[i-1]
            rmse = (sum_left**2) / i + ((sum_total - sum_left)**2) / (n-i)

            if rmse > best_rmse:
                best_rmse, best_threshold = rmse, threshold

    if best_rmse != float('-inf'):
        left_class, right_class = np.mean(
            Y[X < best_threshold]), np.mean(Y[X >= best_threshold])
    else:
        best_threshold = X[0] - 0.5
        left_class, right_class = - \
            np.mean(Y[X >= best_threshold]), np.mean(Y[X >= best_threshold])
    if left_class == right_class:
        best_threshold = min(X) - 0.5
        if right_class == 0:
            left_class = -1
        else:
            left_class *= -1

    if np.isnan(left_class):
        if right_class == 0:
            left_class = -1
        else:
            left_class = right_class * -1
        best_threshold -= 0.5

    print(left_class, right_class, best_threshold)

if __name__ == '__main__':
    main()
