from itertools import product
import numpy as np

def main():
    data = list(map(int, input().split()))
    k = int(input())
    mean_val = np.mean(data)
    answer = mean_val

    sum_rest = 0
    counter = 0

    for a, b in product(data, repeat=2):
        if a != b:
            sum_rest += b
        counter += 1

    sum_rest /= counter

    answer += sum_rest * (k - 1)
    print(answer)

if __name__ == "__main__":
    main()