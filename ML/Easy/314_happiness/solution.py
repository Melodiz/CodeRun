import numpy as np

def read_input():
    data = []
    n, k = map(int, input().split())
    for _ in range(n):
        values = list(map(float, input().split()))
        x_i, a_i, b_i = values[:k], values[-2], values[-1]
        data.append((x_i, a_i, b_i))
    return data

def main():
    # Read data from user input
    data = read_input()

    # Calculate t_i and w_i
    t_values = []
    w_values = []

    for x_i, a_i, b_i in data:
        t_i = a_i / b_i
        w_i = b_i
        t_values.append(t_i)
        w_values.append(w_i)

    t_values = np.array(t_values)
    w_values = np.array(w_values)

    # Calculate the optimal p for MSE
    p_mse = np.sum(w_values * t_values) / np.sum(w_values)

    # Calculate the optimal p for MSLE
    p_msle = np.exp(np.sum(w_values * np.log(1 + t_values)) / np.sum(w_values)) - 1

    # Calculate the optimal p for LogLoss
    p_logloss = np.sum(w_values * t_values) / np.sum(w_values)

    # Print the results
    print(p_mse, p_msle, p_logloss)

if __name__ == "__main__":
    main()