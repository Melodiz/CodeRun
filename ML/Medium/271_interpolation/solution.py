import numpy as np
from sklearn.linear_model import LinearRegression


def preprocess_data(X):
    # given [x1, x2, x3, x4, x5]
    # return [x1^2, x2^2, x3^2, x4^2, x5^2, x1*x2, x1*x3, x1*x4, x1*x5, x2*x3, 
    # x2*x4, x2*x5, x3*x4, x3*x5, x4*x5, x1, x2, x3, x4, x5, 1]
    result = []
    for x in X:
        result.append([x[0]**2, x[1]**2, x[2]**2, x[3]**2, x[4]**2,
                       x[0]*x[1], x[0]*x[2], x[0]*x[3], x[0]*x[4],
                       x[1]*x[2], x[1]*x[3], x[1]*x[4],
                       x[2]*x[3], x[2]*x[4], x[3]*x[4],
                       x[0], x[1], x[2], x[3], x[4], 1])
    return np.array(result)

def main():
    data = [list(map(float, input().split())) for _ in range(2000)]
    X_train = [data[i][:-1] for i in range(1000)]
    y_train = [data[i][-1] for i in range(1000)]
    X_test = data[1000:]

    model = LinearRegression()
    model.fit(preprocess_data(X_train), y_train)
    y_pred = model.predict(preprocess_data(X_test))
    for pred in y_pred:
        print(pred)
    


if __name__ == "__main__":
    main()