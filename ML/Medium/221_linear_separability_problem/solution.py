from sklearn.linear_model import LinearRegression

def main():
    n, m = map(int, input().split())
    X, y = [], []
    for _ in range(n):
        row = list(map(float, input().split()))
        X.append(row[:-1])
        y.append(row[-1])

    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    
    print(' '.join(map(str, model.coef_)))


if __name__ == '__main__':
    main()