import numpy as np


def WeightedMedian(Y_test):
    # calculate weighted median
    if len(Y_test) == 1:
        return np.median(Y_test)
    weights = 1/Y_test
    weights = weights/sum(weights)
    Y_test, weights = np.array(Y_test).squeeze(), np.array(weights).squeeze()
    s_data, s_weights = map(np.array, zip(*sorted(zip(Y_test, weights))))
    midpoint = 0.5 * sum(s_weights)
    if any(weights > midpoint):
        w_median = (Y_test[weights == np.max(weights)])[0]
    else:
        cs_weights = np.cumsum(s_weights)
        idx = np.where(cs_weights <= midpoint)[0][-1]
        if cs_weights[idx] == midpoint:
            w_median = np.mean(s_data[idx:idx+2])
        else:
            w_median = s_data[idx+1]
    return w_median


def main():
    n = int(input())
    Y_test = [int(input()) for _ in range(n)]
    Y_test = np.array(sorted(Y_test))
    print(np.mean(Y_test))  # minimum MSE
    print(np.median(Y_test))  # minimum MAE
    print(WeightedMedian(Y_test))  # weighted median for minimum MAPE


if __name__ == '__main__':
    main()
